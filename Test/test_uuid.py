# UUID stands for Universally Unique Identifier
# uuid7() generates a unique ID based on the current timestamp plus some random bits. Every time you call it, you get a new unique value.

from langchain_core.utils.uuid import uuid7

print(uuid7())