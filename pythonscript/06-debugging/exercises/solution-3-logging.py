#!/usr/bin/env python3
"""
Solution: Exercise 3 - Logging
"""
import logging

print("=" * 60)
print("Solution: Exercise 3 - Logging")
print("=" * 60)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("1. Debug message")
logger.info("2. Info message")
logger.warning("3. Warning message")
logger.error("4. Error message")
logger.critical("5. Critical message")

print("\n✅ Solution completed!")
