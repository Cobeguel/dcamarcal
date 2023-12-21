import unittest
from dcamarcal.calculator import DCAMartingale, DCAMartingaleOrder, Direction


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

    def test_long_EURUSDT(self):
        dca = DCAMartingale.from_float(
            direction=Direction.long,
            base_order_size=20,
            order_size=20,
            max_orders=8,
            price_deviation=1.2,
            target_profit=1.2,
            order_scale=1.2,
            volume_scale=1.5,
            minimum_trade_decimals=4,
        )          
        result = dca.calculate_table(1.0954)
        expected_results = [
            DCAMartingaleOrder.from_float(0, 0, 18.25817053, 20, 1.0954, 1.0954, 1.1085, 1.19591016, 18.25817053, 20),
            DCAMartingaleOrder.from_float(1, 1.2, 18.47992968, 20, 1.0822552, 1.08878792, 1.1018, 1.80593264, 36.73810021, 40),
            DCAMartingaleOrder.from_float(2, 2.64, 28.12988475, 30, 1.06648144, 1.07911475, 1.092, 2.3927805, 64.86798497, 70),
            DCAMartingaleOrder.from_float(3, 4.368, 42.95725666, 45, 1.04755292, 1.06654061, 1.0793, 3.0305936, 107.82524164, 115),
            DCAMartingaleOrder.from_float(4, 6.4416, 65.86402241, 67.5, 1.02483871, 1.050727, 1.0633, 3.75291115, 173.68926405, 182.5),
            DCAMartingaleOrder.from_float(5, 8.92992, 101.49545088, 101.25, 0.99758165, 1.03112558, 1.0434, 4.59294167, 275.18471493, 283.75),
            DCAMartingaleOrder.from_float(6, 11.915904, 157.40410445, 151.875, 0.96487318, 1.00701862, 1.0191, 5.62009734, 432.58881938, 435.625),
            DCAMartingaleOrder.from_float(7, 15.4990848, 246.11801329, 227.8125, 0.92562302, 0.97750231, 0.9892, 6.86856022, 678.70683268, 663.4375),
            DCAMartingaleOrder.from_float(8, 19.79890176, 388.96968671, 341.71875, 0.87852283, 0.94144268, 0.9527, 8.44339695, 1067.67651939, 1005.15625)
        ]

        self.__validate_calculate_table(result, expected_results, decimal_places=4)

    def test_short_EURUSDT(self):
        dca = DCAMartingale.from_float(
            direction=Direction.short,
            base_order_size=20,
            order_size=20,
            max_orders=8,
            price_deviation=1.2,
            target_profit=1.2,
            order_scale=1.2,
            volume_scale=1.5,
            minimum_trade_decimals=4,
        )          
        result = dca.calculate_table(1.0954)
        expected_results = [
            DCAMartingaleOrder.from_float(0, 0, 18.25817053, 20, 1.0954, 1.0954, 1.0823, -1.19591016, 18.25817053, 20),
            DCAMartingaleOrder.from_float(1, 1.2, 18.04167048, 20, 1.1085448, 1.1019332, 1.0888, -1.78114587, 36.29984101, 40),
            DCAMartingaleOrder.from_float(2, 2.64, 26.6828291, 30, 1.12431856, 1.11141683, 1.0981, -2.33195118, 62.98267012, 70),
            DCAMartingaleOrder.from_float(3, 4.368, 39.3615703, 45, 1.14324707, 1.12365873, 1.1102, -2.89063255, 102.34424042, 115),
            DCAMartingaleOrder.from_float(4, 6.4416, 57.89214512, 67.5, 1.16596128, 1.13894231, 1.1253, -3.48736161, 160.23638555, 182.5),
            DCAMartingaleOrder.from_float(5, 8.92992, 84.8545453, 101.25, 1.19321834, 1.15773357, 1.1439, -4.13322037, 245.09093085, 283.75),
            DCAMartingaleOrder.from_float(6, 11.915904, 123.88586207, 151.875, 1.22592681, 1.1806298, 1.1665, -4.84750083, 368.97679293, 435.625),
            DCAMartingaleOrder.from_float(7, 15.4990848, 180.06374168, 227.8125, 1.26517697, 1.20835795, 1.1939, -5.6337553, 549.04053462, 663.4375),
            DCAMartingaleOrder.from_float(8, 19.79890176, 260.40135258, 341.71875, 1.31227716, 1.24178926, 1.2269, -6.50603179, 809.4418872, 1005.15625)
        ]

        self.__validate_calculate_table(result, expected_results, decimal_places=4)

    def test_long_ROSEUSDT(self):
        dca = DCAMartingale.from_float(
            direction=Direction.long,
            base_order_size=20,
            order_size=20,
            max_orders=8,
            price_deviation=1.2,
            target_profit=1.2,
            order_scale=1.2,
            volume_scale=1.5,
            minimum_trade_decimals=5,
        )          
        result = dca.calculate_table(0.09556)
        expected_results = [
            DCAMartingaleOrder.from_float(0, 0, 209.29259104, 20, 0.09556, 0.09556, 0.0967, 1.19296776, 209.29259104, 20),
            DCAMartingaleOrder.from_float(1, 1.2, 211.83460631, 20, 0.09441328, 0.09498317, 0.09612, 1.80771179, 421.12719736, 40),
            DCAMartingaleOrder.from_float(2, 2.64, 322.45160904, 30, 0.09303721, 0.09413931, 0.09526, 2.38913425, 743.5788064, 70),
            DCAMartingaleOrder.from_float(3, 4.368, 492.41710917, 45, 0.09138593, 0.09304237, 0.09415, 3.02460184, 1235.99591557, 115),
            DCAMartingaleOrder.from_float(4, 6.4416, 754.99633893, 67.5, 0.0894044, 0.09166283, 0.09276, 3.75327466, 1990.99225451, 182.5),
            DCAMartingaleOrder.from_float(5, 8.92992, 1163.43780762, 101.25, 0.08702656, 0.08995285, 0.09103, 4.60024062, 3154.43006213, 283.75),
            DCAMartingaleOrder.from_float(6, 11.915904, 1804.3161994, 151.875, 0.08417316, 0.08784982, 0.0889, 5.6156116, 4958.74626153, 435.625),
            DCAMartingaleOrder.from_float(7, 15.4990848, 2821.23976314, 227.8125, 0.08074907, 0.08527489, 0.08629, 6.8619058, 7779.98602468, 663.4375),
            DCAMartingaleOrder.from_float(8, 19.79890176, 4458.74209734, 341.71875, 0.07664016, 0.08212914, 0.08311, 8.441827, 12238.72812202, 1005.15625)
        ]

        self.__validate_calculate_table(result, expected_results, decimal_places=5)


    def test_short_ROSEUSDT(self):
        dca = DCAMartingale.from_float(
            direction=Direction.short,
            base_order_size=20,
            order_size=20,
            max_orders=8,
            price_deviation=1.2,
            target_profit=1.2,
            order_scale=1.2,
            volume_scale=1.5,
            minimum_trade_decimals=5,
        )          
        result = dca.calculate_table(0.09556)
        expected_results = [
            DCAMartingaleOrder.from_float(0, 0, 209.29259104, 20, 0.09556, 0.09556, 0.09442, -1.19296776, 209.29259104, 20),
            DCAMartingaleOrder.from_float(1, 1.2, 206.81086071, 20, 0.09670672, 0.09612994, 0.09498, -1.78552224, 416.10345175, 40),
            DCAMartingaleOrder.from_float(2, 2.64, 305.86407498, 30, 0.09808278, 0.09695726, 0.0958, -2.32740538, 721.96752673, 70),
            DCAMartingaleOrder.from_float(3, 4.368, 451.19991745, 45, 0.09973406, 0.09802522, 0.09685, -2.89175109, 1173.16744419, 115),
            DCAMartingaleOrder.from_float(4, 6.4416, 663.61506663, 67.5, 0.10171559, 0.09935852, 0.09817, -3.48579097, 1836.78251082, 182.5),
            DCAMartingaleOrder.from_float(5, 8.92992, 972.68385228, 101.25, 0.10409343, 0.10099782, 0.09979, -4.13420086, 2809.46636311, 283.75),
            DCAMartingaleOrder.from_float(6, 11.915904, 1420.09808831, 151.875, 0.10694683, 0.10299523, 0.10176, -4.84992166, 4229.56445143, 435.625),
            DCAMartingaleOrder.from_float(7, 15.4990848, 2064.06260618, 227.8125, 0.11037092, 0.10541417, 0.10415, -5.6363806, 6293.62705761, 663.4375),
            DCAMartingaleOrder.from_float(8, 19.79890176, 2984.96904164, 341.71875, 0.11447983, 0.10833063, 0.10704, -6.49881336, 9278.59609925, 1005.15625)
        ]

        self.__validate_calculate_table(result, expected_results, decimal_places=5)
