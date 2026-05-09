import unittest
import subprocess

from gradescope_utils.autograder_utils.decorators import weight, number

class TestBase(unittest.TestCase): 
    def runStudentCode(self, dirname):
        try:
            subprocess.run(['./run_student_code.sh', dirname], check=True, text=True, capture_output=True)
        except subprocess.CalledProcessError as err:
            error_message = str(err.stderr).strip()
            raise AssertionError(f'Unable to run student code on {dirname}: "{error_message}"\n{err.output}'.strip())

    def assertValidVM(self, dirname, name):
        try:
            subprocess.run(['n2tVMEmulator', f'/autograder/source/{dirname}/{name}.tst'], check=True, text=True, capture_output=True)
        except subprocess.CalledProcessError as err:
            error_message = str(err.stderr).strip()
            raise AssertionError(f'Student\'s VM did not pass the provided TST file: "{error_message}"\n{err.output}'.strip())

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
