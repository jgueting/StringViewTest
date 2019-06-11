# StringViewTest
Smaller part of a kivy based violinist app with problems

If you run the fingerdot.py a simple kivy-app opens with a blue dot. Klicking it will enlarge the dot and show a text label on it.
No errors, warnings, whatsoever:

"C:\Program Files (x86)\Python36-32\python.exe" D:/PycharmProjects/StringViewTest/fingerdot.py
[INFO   ] [Logger      ] Record log in C:\Users\jguet\.kivy\logs\kivy_19-06-11_95.txt
[INFO   ] [Kivy        ] v1.11.0
[INFO   ] [Kivy        ] Installed at "C:\Program Files (x86)\Python36-32\lib\site-packages\kivy\__init__.py"
[INFO   ] [Python      ] v3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 12:45:02) [MSC v.1900 32 bit (Intel)]
[INFO   ] [Python      ] Interpreter at "C:\Program Files (x86)\Python36-32\python.exe"
[INFO   ] [deps        ] Successfully imported "kivy_deps.angle" 0.1.9
[INFO   ] [deps        ] Successfully imported "kivy_deps.glew" 0.1.12
[INFO   ] [deps        ] Successfully imported "kivy_deps.sdl2" 0.1.22
[INFO   ] [Factory     ] 184 symbols loaded
[DEBUG  ] [Cache       ] register <kv.image> with limit=None, timeout=60
[DEBUG  ] [Cache       ] register <kv.atlas> with limit=None, timeout=None
[INFO   ] [Image       ] Providers: img_tex, img_dds, img_sdl2, img_gif (img_pil, img_ffpyplayer ignored)
[DEBUG  ] [Cache       ] register <kv.texture> with limit=1000, timeout=60
[DEBUG  ] [Cache       ] register <kv.shader> with limit=1000, timeout=3600
[DEBUG  ] [Cache       ] register <kv.lang> with limit=None, timeout=None
[DEBUG  ] [App         ] Loading kv <D:/PycharmProjects/StringViewTest\fingerdot.kv>
[DEBUG  ] [App         ] kv <D:/PycharmProjects/StringViewTest\fingerdot.kv> not found
[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL" graphics system
[INFO   ] [GL          ] GLEW initialization succeeded
[DEBUG  ] [GL          ] available extensions: b'GL_3DFX_texture_compression_FXT1 GL_AMD_depth_clamp_separate GL_AMD_vertex_shader_layer GL_AMD_vertex_shader_viewport_index GL_ARB_ES2_compatibility GL_ARB_ES3_1_compatibility GL_ARB_ES3_compatibility GL_ARB_arrays_of_arrays GL_ARB_base_instance GL_ARB_bindless_texture GL_ARB_blend_func_extended GL_ARB_buffer_storage GL_ARB_cl_event GL_ARB_clear_buffer_object GL_ARB_clear_texture GL_ARB_clip_control GL_ARB_color_buffer_float GL_ARB_compatibility GL_ARB_compressed_texture_pixel_storage GL_ARB_compute_shader GL_ARB_conditional_render_inverted GL_ARB_conservative_depth GL_ARB_copy_buffer GL_ARB_copy_image GL_ARB_cull_distance GL_ARB_debug_output GL_ARB_depth_buffer_float GL_ARB_depth_clamp GL_ARB_depth_texture GL_ARB_derivative_control GL_ARB_direct_state_access GL_ARB_draw_buffers GL_ARB_draw_buffers_blend GL_ARB_draw_elements_base_vertex GL_ARB_draw_indirect GL_ARB_draw_instanced GL_ARB_enhanced_layouts GL_ARB_explicit_attrib_location GL_ARB_explicit_uniform_location GL_ARB_fragment_coord_conventions GL_ARB_fragment_layer_viewport GL_ARB_fragment_program GL_ARB_fragment_program_shadow GL_ARB_fragment_shader GL_ARB_fragment_shader_interlock GL_ARB_framebuffer_no_attachments GL_ARB_framebuffer_object GL_ARB_framebuffer_sRGB GL_ARB_geometry_shader4 GL_ARB_get_program_binary GL_ARB_get_texture_sub_image GL_ARB_gpu_shader5 GL_ARB_gpu_shader_fp64 GL_ARB_half_float_pixel GL_ARB_half_float_vertex GL_ARB_indirect_parameters GL_ARB_instanced_arrays GL_ARB_internalformat_query GL_ARB_internalformat_query2 GL_ARB_invalidate_subdata GL_ARB_map_buffer_alignment GL_ARB_map_buffer_range GL_ARB_multi_bind GL_ARB_multi_draw_indirect GL_ARB_multisample GL_ARB_multitexture GL_ARB_occlusion_query GL_ARB_occlusion_query2 GL_ARB_pixel_buffer_object GL_ARB_point_parameters GL_ARB_point_sprite GL_ARB_polygon_offset_clamp GL_ARB_post_depth_coverage GL_ARB_program_interface_query GL_ARB_provoking_vertex GL_ARB_query_buffer_object GL_ARB_robust_buffer_access_behavior GL_ARB_robustness GL_ARB_robustness_isolation GL_ARB_sample_shading GL_ARB_sampler_objects GL_ARB_seamless_cube_map GL_ARB_seamless_cubemap_per_texture GL_ARB_separate_shader_objects GL_ARB_shader_atomic_counter_ops GL_ARB_shader_atomic_counters GL_ARB_shader_bit_encoding GL_ARB_shader_draw_parameters GL_ARB_shader_group_vote GL_ARB_shader_image_load_store GL_ARB_shader_image_size GL_ARB_shader_objects GL_ARB_shader_precision GL_ARB_shader_stencil_export GL_ARB_shader_storage_buffer_object GL_ARB_shader_subroutine GL_ARB_shader_texture_image_samples GL_ARB_shading_language_100 GL_ARB_shading_language_420pack GL_ARB_shading_language_packing GL_ARB_shadow GL_ARB_stencil_texturing GL_ARB_sync GL_ARB_tessellation_shader GL_ARB_texture_barrier GL_ARB_texture_border_clamp GL_ARB_texture_buffer_object GL_ARB_texture_buffer_object_rgb32 GL_ARB_texture_buffer_range GL_ARB_texture_compression GL_ARB_texture_compression_bptc GL_ARB_texture_compression_rgtc GL_ARB_texture_cube_map GL_ARB_texture_cube_map_array GL_ARB_texture_env_add GL_ARB_texture_env_combine GL_ARB_texture_env_crossbar GL_ARB_texture_env_dot3 GL_ARB_texture_float GL_ARB_texture_gather GL_ARB_texture_mirror_clamp_to_edge GL_ARB_texture_mirrored_repeat GL_ARB_texture_multisample GL_ARB_texture_non_power_of_two GL_ARB_texture_query_levels GL_ARB_texture_query_lod GL_ARB_texture_rectangle GL_ARB_texture_rg GL_ARB_texture_rgb10_a2ui GL_ARB_texture_stencil8 GL_ARB_texture_storage GL_ARB_texture_storage_multisample GL_ARB_texture_swizzle GL_ARB_texture_view GL_ARB_timer_query GL_ARB_transform_feedback2 GL_ARB_transform_feedback3 GL_ARB_transform_feedback_instanced GL_ARB_transpose_matrix GL_ARB_uniform_buffer_object GL_ARB_vertex_array_bgra GL_ARB_vertex_array_object GL_ARB_vertex_attrib_64bit GL_ARB_vertex_attrib_binding GL_ARB_vertex_buffer_object GL_ARB_vertex_program GL_ARB_vertex_shader GL_ARB_vertex_type_10f_11f_11f_rev GL_ARB_vertex_type_2_10_10_10_rev GL_ARB_viewport_array GL_ARB_window_pos GL_ATI_separate_stencil GL_EXT_abgr GL_EXT_bgra GL_EXT_blend_color GL_EXT_blend_equation_separate GL_EXT_blend_func_separate GL_EXT_blend_minmax GL_EXT_blend_subtract GL_EXT_clip_volume_hint GL_EXT_compiled_vertex_array GL_EXT_direct_state_access GL_EXT_draw_buffers2 GL_EXT_draw_range_elements GL_EXT_fog_coord GL_EXT_framebuffer_blit GL_EXT_framebuffer_multisample GL_EXT_framebuffer_object GL_EXT_geometry_shader4 GL_EXT_gpu_program_parameters GL_EXT_gpu_shader4 GL_EXT_multi_draw_arrays GL_EXT_packed_depth_stencil GL_EXT_packed_float GL_EXT_packed_pixels GL_EXT_polygon_offset_clamp GL_EXT_rescale_normal GL_EXT_secondary_color GL_EXT_separate_specular_color GL_EXT_shader_framebuffer_fetch GL_EXT_shader_integer_mix GL_EXT_shadow_funcs GL_EXT_stencil_two_side GL_EXT_stencil_wrap GL_EXT_texture3D GL_EXT_texture_array GL_EXT_texture_compression_s3tc GL_EXT_texture_edge_clamp GL_EXT_texture_env_add GL_EXT_texture_env_combine GL_EXT_texture_filter_anisotropic GL_EXT_texture_integer GL_EXT_texture_lod_bias GL_EXT_texture_rectangle GL_EXT_texture_sRGB GL_EXT_texture_sRGB_decode GL_EXT_texture_shared_exponent GL_EXT_texture_snorm GL_EXT_texture_storage GL_EXT_texture_swizzle GL_EXT_timer_query GL_EXT_transform_feedback GL_IBM_texture_mirrored_repeat GL_INTEL_conservative_rasterization GL_INTEL_fragment_shader_ordering GL_INTEL_framebuffer_CMAA GL_INTEL_map_texture GL_INTEL_multi_rate_fragment_shader GL_INTEL_performance_query GL_KHR_blend_equation_advanced GL_KHR_blend_equation_advanced_coherent GL_KHR_context_flush_control GL_KHR_debug GL_KHR_texture_compression_astc_hdr GL_KHR_texture_compression_astc_ldr GL_NV_blend_square GL_NV_conditional_render GL_NV_primitive_restart GL_NV_texgen_reflection GL_SGIS_generate_mipmap GL_SGIS_texture_edge_clamp GL_SGIS_texture_lod GL_SUN_multi_draw_arrays GL_WIN_swap_hint WGL_EXT_swap_control'
[DEBUG  ] [GL          ] glShaderBinary is not available
[INFO   ] [GL          ] Backend used <glew>
[INFO   ] [GL          ] OpenGL version <b'4.5.0 - Build 25.20.100.6373'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel(R) UHD Graphics 620'>
[INFO   ] [GL          ] OpenGL parsed version: 4, 5
[INFO   ] [GL          ] Shading version <b'4.50 - Build 25.20.100.6373'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <32>
[DEBUG  ] [Shader      ] Fragment compiled successfully
[DEBUG  ] [Shader      ] Vertex compiled successfully
[DEBUG  ] [ImageSDL2   ] Load <C:\Program Files (x86)\Python36-32\lib\site-packages\kivy\data\glsl\default.png>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO   ] [Text        ] Provider: sdl2
[DEBUG  ] [Resource    ] add <C:\windows\Fonts> in path list
[DEBUG  ] [Resource    ] add <C:\Program Files (x86)\Python36-32\lib\site-packages\kivy\data\fonts> in path list
[DEBUG  ] [Base        ] Create provider from mouse
[DEBUG  ] [Base        ] Create provider from wm_touch
[DEBUG  ] [Base        ] Create provider from wm_pen
[INFO   ] [Base        ] Start application main loop
[INFO   ] [GL          ] NPOT texture support is available
[INFO   ] [WindowSDL   ] exiting mainloop and closing.
[INFO   ] [Base        ] Leaving application in progress...

Process finished with exit code 0


If you run the stringview.py a simplified violin string appears with several of those dots. Just opening the app shows lots of
Exeptions ignored by kivy, yet, they create havy performance issues (especially if I use more than on StringView in the full app).
The ignored exeptions disapear, if I do not use Fingerdots in the StringView.
The messages a created on Windows, yet they appear to be very similar on Ubuntu (same machine)

"C:\Program Files (x86)\Python36-32\python.exe" D:/PycharmProjects/StringViewTest/stringview.py
[INFO   ] [Logger      ] Record log in C:\Users\jguet\.kivy\logs\kivy_19-06-11_96.txt
[INFO   ] [Kivy        ] v1.11.0
[INFO   ] [Kivy        ] Installed at "C:\Program Files (x86)\Python36-32\lib\site-packages\kivy\__init__.py"
[INFO   ] [Python      ] v3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 12:45:02) [MSC v.1900 32 bit (Intel)]
[INFO   ] [Python      ] Interpreter at "C:\Program Files (x86)\Python36-32\python.exe"
[INFO   ] [deps        ] Successfully imported "kivy_deps.angle" 0.1.9
[INFO   ] [deps        ] Successfully imported "kivy_deps.glew" 0.1.12
[INFO   ] [deps        ] Successfully imported "kivy_deps.sdl2" 0.1.22
[INFO   ] [Factory     ] 184 symbols loaded
[DEBUG  ] [Cache       ] register <kv.image> with limit=None, timeout=60
[DEBUG  ] [Cache       ] register <kv.atlas> with limit=None, timeout=None
[INFO   ] [Image       ] Providers: img_tex, img_dds, img_sdl2, img_gif (img_pil, img_ffpyplayer ignored)
[DEBUG  ] [Cache       ] register <kv.texture> with limit=1000, timeout=60
[DEBUG  ] [Cache       ] register <kv.shader> with limit=1000, timeout=3600
[DEBUG  ] [Cache       ] register <kv.lang> with limit=None, timeout=None
[DEBUG  ] [App         ] Loading kv <D:/PycharmProjects/StringViewTest\stringview.kv>
[DEBUG  ] [App         ] kv <D:/PycharmProjects/StringViewTest\stringview.kv> not found
[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL" graphics system
[INFO   ] [GL          ] GLEW initialization succeeded
[DEBUG  ] [GL          ] available extensions: b'GL_3DFX_texture_compression_FXT1 GL_AMD_depth_clamp_separate GL_AMD_vertex_shader_layer GL_AMD_vertex_shader_viewport_index GL_ARB_ES2_compatibility GL_ARB_ES3_1_compatibility GL_ARB_ES3_compatibility GL_ARB_arrays_of_arrays GL_ARB_base_instance GL_ARB_bindless_texture GL_ARB_blend_func_extended GL_ARB_buffer_storage GL_ARB_cl_event GL_ARB_clear_buffer_object GL_ARB_clear_texture GL_ARB_clip_control GL_ARB_color_buffer_float GL_ARB_compatibility GL_ARB_compressed_texture_pixel_storage GL_ARB_compute_shader GL_ARB_conditional_render_inverted GL_ARB_conservative_depth GL_ARB_copy_buffer GL_ARB_copy_image GL_ARB_cull_distance GL_ARB_debug_output GL_ARB_depth_buffer_float GL_ARB_depth_clamp GL_ARB_depth_texture GL_ARB_derivative_control GL_ARB_direct_state_access GL_ARB_draw_buffers GL_ARB_draw_buffers_blend GL_ARB_draw_elements_base_vertex GL_ARB_draw_indirect GL_ARB_draw_instanced GL_ARB_enhanced_layouts GL_ARB_explicit_attrib_location GL_ARB_explicit_uniform_location GL_ARB_fragment_coord_conventions GL_ARB_fragment_layer_viewport GL_ARB_fragment_program GL_ARB_fragment_program_shadow GL_ARB_fragment_shader GL_ARB_fragment_shader_interlock GL_ARB_framebuffer_no_attachments GL_ARB_framebuffer_object GL_ARB_framebuffer_sRGB GL_ARB_geometry_shader4 GL_ARB_get_program_binary GL_ARB_get_texture_sub_image GL_ARB_gpu_shader5 GL_ARB_gpu_shader_fp64 GL_ARB_half_float_pixel GL_ARB_half_float_vertex GL_ARB_indirect_parameters GL_ARB_instanced_arrays GL_ARB_internalformat_query GL_ARB_internalformat_query2 GL_ARB_invalidate_subdata GL_ARB_map_buffer_alignment GL_ARB_map_buffer_range GL_ARB_multi_bind GL_ARB_multi_draw_indirect GL_ARB_multisample GL_ARB_multitexture GL_ARB_occlusion_query GL_ARB_occlusion_query2 GL_ARB_pixel_buffer_object GL_ARB_point_parameters GL_ARB_point_sprite GL_ARB_polygon_offset_clamp GL_ARB_post_depth_coverage GL_ARB_program_interface_query GL_ARB_provoking_vertex GL_ARB_query_buffer_object GL_ARB_robust_buffer_access_behavior GL_ARB_robustness GL_ARB_robustness_isolation GL_ARB_sample_shading GL_ARB_sampler_objects GL_ARB_seamless_cube_map GL_ARB_seamless_cubemap_per_texture GL_ARB_separate_shader_objects GL_ARB_shader_atomic_counter_ops GL_ARB_shader_atomic_counters GL_ARB_shader_bit_encoding GL_ARB_shader_draw_parameters GL_ARB_shader_group_vote GL_ARB_shader_image_load_store GL_ARB_shader_image_size GL_ARB_shader_objects GL_ARB_shader_precision GL_ARB_shader_stencil_export GL_ARB_shader_storage_buffer_object GL_ARB_shader_subroutine GL_ARB_shader_texture_image_samples GL_ARB_shading_language_100 GL_ARB_shading_language_420pack GL_ARB_shading_language_packing GL_ARB_shadow GL_ARB_stencil_texturing GL_ARB_sync GL_ARB_tessellation_shader GL_ARB_texture_barrier GL_ARB_texture_border_clamp GL_ARB_texture_buffer_object GL_ARB_texture_buffer_object_rgb32 GL_ARB_texture_buffer_range GL_ARB_texture_compression GL_ARB_texture_compression_bptc GL_ARB_texture_compression_rgtc GL_ARB_texture_cube_map GL_ARB_texture_cube_map_array GL_ARB_texture_env_add GL_ARB_texture_env_combine GL_ARB_texture_env_crossbar GL_ARB_texture_env_dot3 GL_ARB_texture_float GL_ARB_texture_gather GL_ARB_texture_mirror_clamp_to_edge GL_ARB_texture_mirrored_repeat GL_ARB_texture_multisample GL_ARB_texture_non_power_of_two GL_ARB_texture_query_levels GL_ARB_texture_query_lod GL_ARB_texture_rectangle GL_ARB_texture_rg GL_ARB_texture_rgb10_a2ui GL_ARB_texture_stencil8 GL_ARB_texture_storage GL_ARB_texture_storage_multisample GL_ARB_texture_swizzle GL_ARB_texture_view GL_ARB_timer_query GL_ARB_transform_feedback2 GL_ARB_transform_feedback3 GL_ARB_transform_feedback_instanced GL_ARB_transpose_matrix GL_ARB_uniform_buffer_object GL_ARB_vertex_array_bgra GL_ARB_vertex_array_object GL_ARB_vertex_attrib_64bit GL_ARB_vertex_attrib_binding GL_ARB_vertex_buffer_object GL_ARB_vertex_program GL_ARB_vertex_shader GL_ARB_vertex_type_10f_11f_11f_rev GL_ARB_vertex_type_2_10_10_10_rev GL_ARB_viewport_array GL_ARB_window_pos GL_ATI_separate_stencil GL_EXT_abgr GL_EXT_bgra GL_EXT_blend_color GL_EXT_blend_equation_separate GL_EXT_blend_func_separate GL_EXT_blend_minmax GL_EXT_blend_subtract GL_EXT_clip_volume_hint GL_EXT_compiled_vertex_array GL_EXT_direct_state_access GL_EXT_draw_buffers2 GL_EXT_draw_range_elements GL_EXT_fog_coord GL_EXT_framebuffer_blit GL_EXT_framebuffer_multisample GL_EXT_framebuffer_object GL_EXT_geometry_shader4 GL_EXT_gpu_program_parameters GL_EXT_gpu_shader4 GL_EXT_multi_draw_arrays GL_EXT_packed_depth_stencil GL_EXT_packed_float GL_EXT_packed_pixels GL_EXT_polygon_offset_clamp GL_EXT_rescale_normal GL_EXT_secondary_color GL_EXT_separate_specular_color GL_EXT_shader_framebuffer_fetch GL_EXT_shader_integer_mix GL_EXT_shadow_funcs GL_EXT_stencil_two_side GL_EXT_stencil_wrap GL_EXT_texture3D GL_EXT_texture_array GL_EXT_texture_compression_s3tc GL_EXT_texture_edge_clamp GL_EXT_texture_env_add GL_EXT_texture_env_combine GL_EXT_texture_filter_anisotropic GL_EXT_texture_integer GL_EXT_texture_lod_bias GL_EXT_texture_rectangle GL_EXT_texture_sRGB GL_EXT_texture_sRGB_decode GL_EXT_texture_shared_exponent GL_EXT_texture_snorm GL_EXT_texture_storage GL_EXT_texture_swizzle GL_EXT_timer_query GL_EXT_transform_feedback GL_IBM_texture_mirrored_repeat GL_INTEL_conservative_rasterization GL_INTEL_fragment_shader_ordering GL_INTEL_framebuffer_CMAA GL_INTEL_map_texture GL_INTEL_multi_rate_fragment_shader GL_INTEL_performance_query GL_KHR_blend_equation_advanced GL_KHR_blend_equation_advanced_coherent GL_KHR_context_flush_control GL_KHR_debug GL_KHR_texture_compression_astc_hdr GL_KHR_texture_compression_astc_ldr GL_NV_blend_square GL_NV_conditional_render GL_NV_primitive_restart GL_NV_texgen_reflection GL_SGIS_generate_mipmap GL_SGIS_texture_edge_clamp GL_SGIS_texture_lod GL_SUN_multi_draw_arrays GL_WIN_swap_hint WGL_EXT_swap_control'
[DEBUG  ] [GL          ] glShaderBinary is not available
[INFO   ] [GL          ] Backend used <glew>
[INFO   ] [GL          ] OpenGL version <b'4.5.0 - Build 25.20.100.6373'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel(R) UHD Graphics 620'>
[INFO   ] [GL          ] OpenGL parsed version: 4, 5
[INFO   ] [GL          ] Shading version <b'4.50 - Build 25.20.100.6373'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <32>
[DEBUG  ] [Shader      ] Fragment compiled successfully
[DEBUG  ] [Shader      ] Vertex compiled successfully
[DEBUG  ] [ImageSDL2   ] Load <C:\Program Files (x86)\Python36-32\lib\site-packages\kivy\data\glsl\default.png>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[DEBUG  ] [ImageSDL2   ] Load <D:\PycharmProjects\StringViewTest\images\left_gradient.png>
[INFO   ] [GL          ] NPOT texture support is available
[DEBUG  ] [ImageSDL2   ] Load <D:\PycharmProjects\StringViewTest\images\right_gradient.png>
[INFO   ] [Text        ] Provider: sdl2
[DEBUG  ] [Resource    ] add <C:\windows\Fonts> in path list
[DEBUG  ] [Resource    ] add <C:\Program Files (x86)\Python36-32\lib\site-packages\kivy\data\fonts> in path list
[DEBUG  ] [Base        ] Create provider from mouse
[DEBUG  ] [Base        ] Create provider from wm_touch
[DEBUG  ] [Base        ] Create provider from wm_pen
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
[INFO   ] [WindowSDL   ] exiting mainloop and closing.
[INFO   ] [Base        ] Leaving application in progress...

Process finished with exit code 0
