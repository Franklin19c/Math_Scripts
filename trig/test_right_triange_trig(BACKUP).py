import right_triangle_trig
import unittest

class TestRight_triangle_trig(unittest.TestCase):

    def test_adjside_oppside(self):
        self.assertDictEqual(right_triangle_trig.adjside_oppside({'adj_side': 45, 'opp_side': 45}), {'adj_side': 45, 'opp_side': 45, 'hyp': 63.64, 'adj_angle': 45, 'opp_angle': 45})
        self.assertDictEqual(right_triangle_trig.adjside_oppside({'adj_side': 157, 'opp_side': 1380}), {'adj_side': 157, 'opp_side': 1380, 'hyp': 1388.9, 'adj_angle': 83.51, 'opp_angle': 6.49})

    def test_adjside_hyp(self):
        pass
        #self.assertDictEqual(right_triangle_trig.adjside_hyp())

    def test_adjside_adjangle(self):
        pass
        #self.assertDictEqual(right_triangle_trig.adjside_adjangle())

    def test_adjside_oppangle(self):
        pass
        #self.assertDictEqual(right_triangle_trig.adjside_oppangle())

    def test_oppside_hyp(self):
        pass

    def test_oppside_adjangle(self):
        pass

    def test_oppside_oppangle(self):
        pass

    def test_hyp_adjangle(self):
        pass

    def test_hyp_opp_angle(self):
        pass

    def test_adjangle_oppangle(self):
        pass


if __name__ == "__main__":
    unittest.main()
