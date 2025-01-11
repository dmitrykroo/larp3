import unittest
from unittest.mock import MagicMock
from src.models.data_models import NFT, User, Valuation, Report

class TestDataModels(unittest.TestCase):
    def test_nft_model(self):
        nft = NFT(
            id="nft123",
            name="Art Piece",
            description="A unique art piece.",
            creator="ArtistXYZ",
            collection="ModernArt",
            rarity="rare",
            historical_prices=[1000, 1500, 2000],
            metadata={"color": "blue", "size": "large"}
        )
        self.assertEqual(nft.id, "nft123")
        self.assertEqual(nft.name, "Art Piece")
        self.assertEqual(nft.rarity, "rare")
        self.assertEqual(len(nft.historical_prices), 3)
        self.assertIn("color", nft.metadata)

    def test_user_model(self):
        user = User(
            id="user123",
            username="john_doe",
            email="john@example.com",
            registered_at="2025-01-01T12:00:00Z",
            nfts_owned=["nft123", "nft456"]
        )
        self.assertEqual(user.id, "user123")
        self.assertEqual(user.username, "john_doe")
        self.assertIn("nft123", user.nfts_owned)

    def test_valuation_model(self):
        valuation = Valuation(
            nft_id="nft123",
            user_id="user123",
            valuation=2500.0,
            timestamp="2025-01-24T15:30:00Z"
        )
        self.assertEqual(valuation.nft_id, "nft123")
        self.assertEqual(valuation.user_id, "user123")
        self.assertEqual(valuation.valuation, 2500.0)

    def test_report_model(self):
        valuation1 = Valuation(
            nft_id="nft123",
            user_id="user123",
            valuation=2500.0,
            timestamp="2025-01-24T15:30:00Z"
        )
        valuation2 = Valuation(
            nft_id="nft456",
            user_id="user123",
            valuation=3000.0,
            timestamp="2025-01-24T16:00:00Z"
        )
        report = Report(
            user_id="user123",
            generated_at="2025-01-24T16:30:00Z",
            valuations=[valuation1, valuation2],
            insights="Positive market trends observed."
        )
        self.assertEqual(report.user_id, "user123")
        self.assertEqual(len(report.valuations), 2)
        self.assertEqual(report.insights, "Positive market trends observed.")

if __name__ == '__main__':
    unittest.main()
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                                                   
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
