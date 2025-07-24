import redis
import pickle
from typing import Optional
from ..utils.logger import setup_logger

class STTCache:
    """Optional caching for STT outputs."""
    
    def __init__(self, enabled: bool = False, redis_url: Optional[str] = None):
        self.enabled = enabled
        self.logger = setup_logger()
        self.redis_client = None
        if enabled and redis_url:
            try:
                self.redis_client = redis.Redis.from_url(redis_url)
                self.logger.info("Redis cache initialized")
            except redis.RedisError as e:
                self.logger.error(f"Failed to initialize Redis cache: {e}")
                self.enabled = False
    
    def get(self, key: str) -> Optional[bytes]:
        if not self.enabled or not self.redis_client:
            return None
        try:
            return self.redis_client.get(key)
        except redis.RedisError as e:
            self.logger.error(f"Cache get error: {e}")
            return None
    
    def set(self, key: str, value: bytes, ttl: int = 3600) -> None:
        if not self.enabled or not self.redis_client:
            return
        try:
            self.redis_client.setex(key, ttl, value)
            self.logger.info(f"Cached key {key} with TTL {ttl}")
        except redis.RedisError as e:
            self.logger.error(f"Cache set error: {e}")