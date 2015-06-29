swig -D"_WIN64" -outdir x64dbg_python\pluginsdk -o x64dbg_python\pluginsdk\__x64dbg.cpp -c++ -python x64dbg.i
python setup.py build