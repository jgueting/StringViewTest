# StringViewTest
Smaller part of a kivy based violinist app with problems

If you run the fingerdot.py a simple kivy-app opens with a blue dot. Klicking it will enlarge the dot and show a text label on it.
No errors, warnings, whatsoever:
[INFO   ] [Logger      ] Record log in C:\Users\jguet\.kivy\logs\kivy_19-06-11_92.txt
[INFO   ] [Kivy        ] v1.11.0
[INFO   ] [Kivy        ] Installed at "C:\Program Files (x86)\Python36-32\lib\site-packages\kivy\__init__.py"
[INFO   ] [Python      ] v3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 12:45:02) [MSC v.1900 32 bit (Intel)]
[INFO   ] [Python      ] Interpreter at "C:\Program Files (x86)\Python36-32\python.exe"
[INFO   ] [deps        ] Successfully imported "kivy_deps.angle" 0.1.9
[INFO   ] [deps        ] Successfully imported "kivy_deps.glew" 0.1.12
[INFO   ] [deps        ] Successfully imported "kivy_deps.sdl2" 0.1.22
[INFO   ] [Factory     ] 184 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_dds, img_sdl2, img_gif (img_pil, img_ffpyplayer ignored)
[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL" graphics system
[INFO   ] [GL          ] GLEW initialization succeeded
[INFO   ] [GL          ] Backend used <glew>
[INFO   ] [GL          ] OpenGL version <b'4.5.0 - Build 25.20.100.6373'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel(R) UHD Graphics 620'>
[INFO   ] [GL          ] OpenGL parsed version: 4, 5
[INFO   ] [GL          ] Shading version <b'4.50 - Build 25.20.100.6373'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <32>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO   ] [Text        ] Provider: sdl2
[INFO   ] [Base        ] Start application main loop
[INFO   ] [GL          ] NPOT texture support is available
[INFO   ] [WindowSDL   ] exiting mainloop and closing.
[INFO   ] [Base        ] Leaving application in progress...


If you run the stringview.py a simplified violin string appears with several of those dots. Just opening the app shows lots of
Exeptions ignored by kivy, yet, they create havy performance issues (especially if I use more than on StringView in the full app).
The ignored exeptions disapear, if I do not use Fingerdots in the StringView.

[INFO   ] [Logger      ] Record log in C:\Users\jguet\.kivy\logs\kivy_19-06-11_93.txt
[INFO   ] [Kivy        ] v1.11.0
[INFO   ] [Kivy        ] Installed at "C:\Program Files (x86)\Python36-32\lib\site-packages\kivy\__init__.py"
[INFO   ] [Python      ] v3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 12:45:02) [MSC v.1900 32 bit (Intel)]
[INFO   ] [Python      ] Interpreter at "C:\Program Files (x86)\Python36-32\python.exe"
[INFO   ] [deps        ] Successfully imported "kivy_deps.angle" 0.1.9
[INFO   ] [deps        ] Successfully imported "kivy_deps.glew" 0.1.12
[INFO   ] [deps        ] Successfully imported "kivy_deps.sdl2" 0.1.22
[INFO   ] [Factory     ] 184 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_dds, img_sdl2, img_gif (img_pil, img_ffpyplayer ignored)
[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL" graphics system
[INFO   ] [GL          ] GLEW initialization succeeded
[INFO   ] [GL          ] Backend used <glew>
[INFO   ] [GL          ] OpenGL version <b'4.5.0 - Build 25.20.100.6373'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel(R) UHD Graphics 620'>
[INFO   ] [GL          ] OpenGL parsed version: 4, 5
[INFO   ] [GL          ] Shading version <b'4.50 - Build 25.20.100.6373'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <32>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO   ] [GL          ] NPOT texture support is available
[INFO   ] [Text        ] Provider: sdl2
[INFO   ] [Base        ] Start application main loop
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.RenderContext.set_state'
 Traceback (most recent call last):
   File "kivy\graphics\shader.pyx", line 245, in kivy.graphics.shader.Shader.set_uniform
   File "kivy\graphics\shader.pyx", line 284, in kivy.graphics.shader.Shader.upload_uniform
 IndexError: list index out of range
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
 Exception ignored in: 'kivy.graphics.instructions.InstructionGroup.build'
 Traceback (most recent call last):
   File "kivy\graphics\compiler.pyx", line 143, in kivy.graphics.compiler.GraphicsCompiler.compile
   File "kivy\graphics\vertex_instructions_line.pxi", line 195, in kivy.graphics.vertex_instructions.Line.apply
 IndexError: list index out of range
