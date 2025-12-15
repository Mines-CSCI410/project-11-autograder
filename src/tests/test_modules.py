import unittest
import subprocess

from gradescope_utils.autograder_utils.decorators import weight, number

class TestBase(unittest.TestCase): 
    def runStudentCode(self, dirname):
        res = subprocess.call(['./run_student_code.sh', dirname])
        if res != 0:
            raise AssertionError(f'Unable to run student\'s Jack Compiler on {dirname}!')

    def assertValidVM(self, dirname, name):
        res = subprocess.call(['n2tVMEmulator', f'/autograder/source/{dirname}/{name}.tst'])
        if res != 0:
            raise AssertionError(f'Invalid VM file!')

    def assertCorrectCompiler(self, dirname):
        name = 'Main'
        self.runStudentCode(dirname)
        self.assertValidVM(dirname, name)
        subprocess.run(['mv', f'/autograder/source/{dirname}/{name}.vm', '/autograder/outputs/'])

class TestModules(TestBase): 
    @weight(95/6)
    @number(1)
    def test_average(self):
        self.assertCorrectCompiler('Average')

    @weight(95/6)
    @number(2)
    def test_complex_arrays(self):
        self.assertCorrectCompiler('ComplexArrays')

    @weight(95/6)
    @number(3)
    def test_convert_to_bin(self):
        self.assertCorrectCompiler('ConvertToBin')

    @weight(95/6)
    @number(4)
    def test_pong(self):
        self.assertCorrectCompiler('Pong')

    @weight(95/6)
    @number(5)
    def test_seven(self):
        self.assertCorrectCompiler('Seven')

    @weight(95/6)
    @number(6)
    def test_square(self):
        self.assertCorrectCompiler('Square')
