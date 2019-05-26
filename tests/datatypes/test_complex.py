from ..utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase, \
    MagicMethodFunctionTestCase

import unittest


class ComplexTests(TranspileTestCase):
    @unittest.expectedFailure
    def test_setattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            try:
                x.attr = 42
            except AttributeError as e:
                print(e)
            print('Done.')
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            try:
                print(x.attr)
            except AttributeError as e:
                print(e)
            print('Done.')
            """)


class MagicMethodFunctionTests(MagicMethodFunctionTestCase, TranspileTestCase):
    data_type = 'complex'
    MagicMethodFunctionTestCase._add_tests(vars(), complex)

    not_implemented = [
        "test__pow__complex",
        "test__pow__float",
        "test__pow__int",

        "test__rpow__bool",
        "test__rpow__complex",
        "test__rpow__float",
        "test__rpow__int",
        "test__rsub__bool",
        "test__rsub__complex",
        "test__rsub__float",
        "test__rsub__int",
        "test__rtruediv__bool",
        "test__rtruediv__complex",
        "test__rtruediv__float",
        "test__rtruediv__int",
    ]


class UnaryComplexOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'complex'


class BinaryComplexOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'complex'

    not_implemented = [
        # These two work, but print floats not *quite* right due to JS
        # Python differences
        # TODO: re-implement the Python float printing function.

        'test_power_complex',
        'test_power_float',
        'test_power_int',

        # Incorrect error message shown (unsupported operands vs can't multiply sequence by non-int)
        "test_multiply_bytearray",
        "test_multiply_bytes",
    ]


class InplaceComplexOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'complex'

    not_implemented = [
        # Incorrect error message shown (unsupported operands vs can't multiply sequence by non-int)
        "test_multiply_bytearray",
        "test_multiply_bytes",

        'test_power_complex',
        'test_power_float',
        'test_power_int',
    ]
