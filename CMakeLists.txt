cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(pico-w-base)

pico_sdk_init()

add_executable(pico-w-base
    main.c
)

pico_enable_stdio_usb(pico-w-base 1)
pico_enable_stdio_uart(pico-w-base 0)

pico_add_extra_outputs(pico-w-base)

target_link_libraries(pico-w-base pico_stdlib)
