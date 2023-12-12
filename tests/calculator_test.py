from dcamarcal.calculator import DCAMartingale, DCAMartingaleOrder
import unittest

class TestDCAMartingale(unittest.TestCase):
    
    def __validate_calculate_table(self, result, expected_results, decimal_places=5):
        self.assertEqual(len(result), len(expected_results), "List size not equal")

        for actual, expected in zip(result, expected_results):
            self.assertAlmostEqual(actual.order, expected.order, places=decimal_places, msg="order does not match")
            self.assertAlmostEqual(actual.deviation, expected.deviation, places=decimal_places, msg="deviation does not match")
            self.assertAlmostEqual(actual.size, expected.size, places=decimal_places, msg="size does not match")
            self.assertAlmostEqual(actual.volume, expected.volume, places=decimal_places, msg="volume does not match")
            self.assertAlmostEqual(actual.price, expected.price, places=decimal_places, msg="price does not match")
            self.assertAlmostEqual(actual.average_price, expected.average_price, places=decimal_places, msg="average_price does not match")
            self.assertAlmostEqual(actual.required_price, expected.required_price, places=decimal_places, msg="required_price does not match")
            self.assertAlmostEqual(actual.required_change, expected.required_change, places=decimal_places, msg="required_change does not match")
            self.assertAlmostEqual(actual.total_size, expected.total_size, places=decimal_places, msg="total_size does not match")
            self.assertAlmostEqual(actual.total_volume, expected.total_volume, places=decimal_places, msg="total_volume does not match")

    def test_EURUSDT(self):
        dca = DCAMartingale(
        base_order_size=20,
        order_size=20,
        max_orders=8,
        price_deviation=1.2,
        target_profit=1.2,
        order_scale=1.2,
        volume_scale=1.5,
        minimum_trade_decimals=8,
        initial_price=100
        )          
        result = dca.calculate_table(1.0788)

        expected_results = [
            DCAMartingaleOrder(0, 0.000000, 18.539118, 20.00000, 1.078800, 1.078800, 1.091746, 1.200000, 18.539118, 20.00000),
            DCAMartingaleOrder(1, 1.200000, 18.764289, 20.00000, 1.065854, 1.072288, 1.085156, 1.810865, 37.303407, 40.00000),
            DCAMartingaleOrder(2, 2.640000, 28.562732, 30.00000, 1.050320, 1.062762, 1.075515, 2.398794, 65.866139, 70.00000),
            DCAMartingaleOrder(3, 4.368000, 43.618260, 45.00000, 1.031678, 1.050378, 1.062982, 3.034327, 109.484399, 115.00000),
            DCAMartingaleOrder(4, 6.441600, 66.877503, 67.50000, 1.009308, 1.034804, 1.047222, 3.756397, 176.361902, 182.50000),
            DCAMartingaleOrder(5, 8.929920, 103.057209, 101.25000, 0.982464, 1.015500, 1.027686, 4.602875, 279.419111, 283.75000),
            DCAMartingaleOrder(6, 11.915904, 159.826155, 151.87500, 0.950251, 0.991758, 1.003659, 5.620393, 439.245266, 435.62500),
            DCAMartingaleOrder(7, 15.499085, 249.905146, 227.81250, 0.911596, 0.962689, 0.974241, 6.872054, 689.150412, 663.43750),
            DCAMartingaleOrder(8, 19.798902, 394.954945, 341.71875, 0.865209, 0.927176, 0.938302, 8.447950, 1084.105357, 1005.15625)
        ]

        self.__validate_calculate_table(result, expected_results)
