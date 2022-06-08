class RunCodeInterface:
    def compile_code(self):
        raise NotImplementedError("You must implement compile_code().")

    def execute_code(self):
        raise NotImplementedError("You must implement execute_code().")

class GoCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Go code")

    def execute_code(self):
        print("Execute Go code")


class JavaCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Java code")

    def execute_code(self):
        print("Execute Java code")

def run_code(code : RunCodeInterface):
    code.compile_code()
    code.execute_code()


go = GoCode()
run_code(go)