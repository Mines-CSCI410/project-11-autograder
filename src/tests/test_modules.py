import unittest
import subprocess

from gradescope_utils.autograder_utils.decorators import weight, number

class TestBase(unittest.TestCase): 
    def runStudentCode(self, dirname):
        try:
            process = subprocess.run(['./run_student_code.sh', dirname], check=True, text=True, capture_output=True, timeout=30)
            if len(process.stdout.strip()) > 0:
                print(process.stdout.strip())
            if len(process.stderr.strip()) > 0:
                print(process.stderr.strip())
        except subprocess.CalledProcessError as err:
            error_message = str(err.stderr).strip()
            raise AssertionError(f'Unable to run student code on {dirname}: "{error_message}"\n{err.stdout}'.strip())
        except subprocess.TimeoutExpired as err:
            raise TimeoutError(f'Student code timed out after {err.timeout} seconds:\n{str(err.stdout).strip()}')

    def assertValidVM(self, dirname, name):
        try:
            subprocess.run(['n2tVMEmulator', f'/autograder/source/{dirname}/{name}.tst'], check=True, text=True, capture_output=True, timeout=30)
        except subprocess.CalledProcessError as err:
            error_message = str(err.stderr).strip()
            raise AssertionError(f'Student\'s VM did not pass the provided TST file: "{error_message}"\n{err.stdout}'.strip())
        except subprocess.TimeoutExpired as err:
            raise TimeoutError(f'Emulator timed out out after {err.timeout} seconds:\n{str(err.stdout).strip()}')

    def assertCorrectCompiler(self, dirname):
        name = 'Main'
        self.runStudentCode(dirname)
        self.assertValidVM(dirname, name)

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
