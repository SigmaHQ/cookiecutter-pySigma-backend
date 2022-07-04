import subprocess

subprocess.run(["poetry", "add", "pysigma"])
subprocess.run(["poetry", "add", "-D", "pytest"])
subprocess.run(["poetry", "add", "-D", "pytest-cov"])
subprocess.run(["poetry", "add", "-D", "coverage"])