from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class NFT:
    """
    Data model representing an NFT.
    """
    id: str
    name: str
    description: Optional[str] = None
    creator: Optional[str] = None
    collection: Optional[str] = None
    rarity: Optional[str] = None
    historical_prices: List[float] = field(default_factory=list)
    metadata: Optional[dict] = field(default_factory=dict)

@dataclass
class User:
    """
    Data model representing a User.
    """
    id: str
    username: str
    email: str
    registered_at: str
    nfts_owned: List[str] = field(default_factory=list)

@dataclass
class Valuation:
    """
    Data model representing an NFT Valuation.
    """
    nft_id: str
    user_id: str
    valuation: float
    timestamp: str

@dataclass
class Report:
    """
    Data model representing a User Report.
    """
    user_id: str
    generated_at: str
    valuations: List[Valuation]
    insights: Optional[str] = None
              
              
              
              
              
              
              
              
              
              
