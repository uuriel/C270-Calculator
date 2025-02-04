__________________________________________________________________________ ERROR collecting test_app.py ___________________________________________________________________________
ImportError while importing test module '/home/lucas/C270-Calculator/tests/test_app.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_app.py:2: in <module>
    from app import app
E   ModuleNotFoundError: No module named 'app'
============================================================================= short test summary info =============================================================================
ERROR test_app.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
