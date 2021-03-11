if exist "out_IMG(DELETE)" rmdir "out_IMG(DELETE)" /s /q
if exist bin_output(DELETE).txt del bin_output(DELETE).txt
if exist dat_output(DELETE).txt del dat_output(DELETE).txt
if exist del wsb_output(DELETE).txt del wsb_output(DELETE).txt
if exist patch.xdelta del patch.xdelta
if exist holo_patched.nds del holo_patched.nds
cd..
tool.exe repack --no-redirect
pause