from UltraScriptR import unix
from UltraScriptR import powershell
from UltraScriptR import batch
from UltraScriptR import cmd
from UltraScriptR import append

def main():
     test_unix()
     test_powershell()
     test_batch()
     test_cmd()
     test_append()

def test_unix():
     fname0 = "test"
     str0 = "echo hello from pytest"
     assert unix(fname0, str0) == True, "Function is working"

def test_powershell():
     fname1 = "test"
     str1 = "echo hello from pytest"
     assert powershell(fname1, str1) == True, "Function is working"

def test_batch():
     fname2 = "test"
     str2 = "echo hello from pytest"
     assert batch(fname2, str2) == True, "Function is working"

def test_cmd():
     fname3 = "test"
     str3 = "echo hello from pytest"
     assert cmd(fname3, str3) == True, "Function is working"

def test_append():
     fname4 = "test"
     str4 = "echo hello from pytest"
     assert append(fname4, str4) == True, "Function is working"

