import unittest
from client3 import getDataPoint

#----- Import the getRatio method for my bonus unit tests ------#
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0])[3], 120.84)
    self.assertEqual(getDataPoint(quotes[1])[3], 119.775)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0])[1] > getDataPoint(quotes[0])[2], True)
    self.assertEqual(getDataPoint(quotes[1])[1] > getDataPoint(quotes[1])[2], False)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
     self.assertEqual(getRatio(75, 100), 0.75)
  
  def test_getRatio_priceAzero(self):
     self.assertEqual(getRatio(0, 100), 0)

  def test_getRatio_priceBzero(self):
     self.assertEqual(getRatio(100, 0), None)


if __name__ == '__main__':
    unittest.main()
