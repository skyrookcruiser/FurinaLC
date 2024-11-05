use ohkami::prelude::*;
use tokio::fs;

async fn get_hash(file: &str) -> String {
    let path = format!("./hashes/{}", file);
    println!("GET: {}", path);
    match fs::read_to_string(&path).await {
        Ok(contents) => contents,
        Err(_) => {
            println!("WARN: {} not found.", file);
            String::from("Not Found")
        }
    }
}

async fn get_server_info(file: &str) -> String {
    let path = format!("./server_infos/{}", file);
    println!("GET: {}", path);
    match fs::read_to_string(&path).await {
        Ok(contents) => contents,
        Err(_) => {
            println!("WARN: {} not found.", file);
            String::from("Not Found")
        }
    }
}

async fn get_sound_patch(file: &str) -> String {
    let path = format!("./sound_patches/{}", file);
    println!("GET: {}", path);
    match fs::read_to_string(&path).await {
        Ok(contents) => contents,
        Err(_) => {
            println!("WARN: {} not found.", file);
            String::from("Not Found")
        }
    }
}

async fn post_battlelog() -> String {
    println!("POST: ./log");
    String::from("Log received successfully")
}

#[tokio::main]
async fn main() {
    println!("Listening at 127.0.0.1:2070");
    Ohkami::new((
        "/hash/:file".GET(get_hash),
        "/server_info/:file".GET(get_server_info),
        "/sound_patch/:file".GET(get_sound_patch),
        "/log".POST(post_battlelog),
    ))
    .howl("127.0.0.1:2070")
    .await
}
