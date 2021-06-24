0. preparation: venv, requirements, new project...
1. execute prog
2. execute test_prog() in 'run' and 'debug' mode
3. execute contents of tests dir in 'run' and 'debug' mode
4. difference in #2
5. solutions:
5.1 control paths
5.2 avoid name duplicates
5.3 verify (check __file__, etc.)
6. cmdline variants (PYTHONPATH=tests/modules python -m nose tests.modules.test_prog:TestProg.test_prog)