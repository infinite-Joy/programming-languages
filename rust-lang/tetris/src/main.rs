extern crate sdl2;

use sdl2::pixels::Color;
use sdl2::event::Event;
use sdl2::keyboard::Keycode;
use sdl2::rect::Rect;
use sdl2::render::{Canvas, Texture, TextureCreator};
use std::time::Duration;
use std::thread::sleep;

const TEXTURE_SIZE: u32 = 32;

pub fn main() {
    let sdl_context = sdl2::init().expect("SDL initialization failed");
    let video_subsystem = sdl_context.video().expect("Couldnt get SDL video subsystem.");

    let window = video_subsystem.window("rust sdl2 demo: Video", 800, 600)
        .position_centered()
        .opengl()
        .build()
        .expect("Failed to create window");

    let mut canvas = window.into_canvas()
        .target_texture()
        .present_vsync()
        .build().expect("Failed to convert windows into canvas");

    let tecture_creator: TextureCreator<_> = canvas.texture_creator();

    let mut square_texture: Texture = tecture_creator
        .create_texture_target(None, TEXTURE_SIZE, TEXTURE_SIZE)
        .expect("Failed to create a texture");

    //canvas.set_draw_color(Color::RGB(0, 255, 0));
    //canvas.clear();
    //canvas.present();

    canvas.with_texture_canvas(&mut square_texture, |texture| {
        texture.set_draw_color(Color::RGB(0, 255, 0));
        texture.clear();
    }).expect("Failed to color a texture");

    let mut event_pump = sdl_context.event_pump().expect("Failed to get event pump");

    'running: loop {
        for event in event_pump.poll_iter() {
            match event {
                Event::Quit {..} |
                    Event::KeyDown {keycode: Some(Keycode::Escape), ..} => {
                        break 'running
                    },
                    _ => {}
            }
        }

        // we fill our window with rosy brown
        canvas.set_draw_color(Color::RGB(188,143,143));
        canvas.clear();

        canvas.copy(&square_texture,
                    None,
                    Rect::new(0, 0, TEXTURE_SIZE, TEXTURE_SIZE))
            .expect("couldnt copy texture into window");
        canvas.present();

        // we sleep enough to get 60 fps. if we dont call this the program will
        // take 100% cpu.
        sleep(Duration::new(0, 1_000_000_000u32/60));
    }
}
