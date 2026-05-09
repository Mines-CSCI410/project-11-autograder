import unittest
import subprocess

from gradescope_utils.autograder_utils.decorators import weight, number

class TestBase(unittest.TestCase): 
    def runStudentCode(self, dirname):
        res = subprocess.call(['./run_student_code.sh', dirname])
        if res != 0:
            raise AssertionError(f'Unable to run student\'s Jack Compiler on {dirname}!')

    def assertValidVM(self, dirname, name):
        try:
            subprocess.check_output(['n2tVMEmulator', f'/autograder/source/{dirname}/{name}.tst'], text=True)
        except subprocess.CalledProcessError as err:
            raise AssertionError(f'Student\'s VM did not pass the provided TST file:\n{err.stderr}')

    def assertCorrectCompiler(self, dirname):
        name = 'Main'
        self.runStudentCode(dirname)
        self.assertValidVM(dirname, name)
        subprocess.run(['cp', '-R', f'/autograder/source/{dirname}', '/autograder/outputs/'])

class TestModules(TestBase): 
    @weight(20/6)
    @number(1)
    def test_average_valid_vm(self):
        self.assertCorrectCompiler('Average')

    @weight(20/6)
    @number(2)
    def test_complex_arrays_valid_vm(self):
        self.assertCorrectCompiler('ComplexArrays')

    @weight(20/6)
    @number(3)
    def test_convert_to_bin_valid_vm(self):
        self.assertCorrectCompiler('ConvertToBin')

    @weight(20/6)
    @number(4)
    def test_pong_valid_vm(self):
        self.assertCorrectCompiler('Pong')

    @weight(20/6)
    @number(5)
    def test_seven_valid_vm(self):
        self.assertCorrectCompiler('Seven')

    @weight(20/6)
    @number(6)
    def test_square_valid_vm(self):
        self.assertCorrectCompiler('Square')
