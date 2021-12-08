/**
    Solutions to day 5 of advent of code 2021
    Author: Josefine Klintberg
*/
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashMap;

fn main() {
    // Storing of coordinates, we don't wan't to cause extra memory storage
    // so instead we use a hash-map to only add lines to coordinates that
    // have been represented. E.g. no need to store 0's.
    let mut coordinates = HashMap::<String, i32>::new();
    let mut start;
    let mut end;
    let mut curr;
    let mut input_key;
    let mut diagonal = false;
    let part2 = false;  // Enable for part 2

    // Read in the input file
    if let Ok(lines) = read_lines("./input.txt") {
        for line in lines {
            if let Ok(ip) = line {

                // Parse each line and split by chars
                let vec: Vec<&str> = ip.split(" -> ").collect();
                let first: Vec<&str> = vec[0].split(",").collect();
                let num2 = vec[1].split(",");
                let second: Vec<&str> = num2.collect();

                // Determine the row start and col start
                let row_start = first[0].parse::<i32>().unwrap();
                let row_end = second[0].parse::<i32>().unwrap();
                let col_start = first[1].parse::<i32>().unwrap();
                let col_end = second[1].parse::<i32>().unwrap();

                // Set iteration ranges depending on type of line
                if col_start == col_end{
                    if row_start < row_end{
                        start = row_start;
                        end = row_end;
                    } else{
                        start = row_end;
                        end = row_start;
                    };
                    curr = col_start;
                } else if row_start == row_end {
                    if col_start < col_end{
                        start = col_start;
                        end = col_end;
                    } else{
                        start = col_end;
                        end = col_start;
                    };
                    curr = row_start;
                } else{  // Diagonal line, part 2
                    if part2{
                        if row_start < row_end{
                            start = row_start;
                            end = row_end;
                            curr = col_start;
                        } else{
                            start = row_end;
                            end = row_start;
                            curr = col_end;
                        };
                        diagonal = true;
                    } else {
                        continue;
                    }
                };

                // Iterate over line and insert/update hash-map keys
                for i in start..end + 1 {
                    if diagonal{  // Diagonal line
                        input_key = format!("{}{}{}", i.to_string(), ",", curr.to_string());
                        if start == row_end && col_start <= col_end || start == row_start && col_start > col_end {
                            curr -= 1;
                        } else if start == row_end && col_start > col_end || start == row_start && col_start <= col_end  {
                            curr += 1;
                        };
                    } else if col_start == col_end{  // Vertical line
                        input_key = format!("{}{}{}", i.to_string(), ",", curr.to_string());
                    } else {  // Horizontal line
                        input_key = format!("{}{}{}", curr.to_string(), ",", i.to_string());
                    };

                    if !coordinates.contains_key(&input_key) {
                        coordinates.insert(input_key, 1);
                    } else {
                        let stat = coordinates.entry(input_key).or_insert(1);
                        *stat += 1;
                    };
                };
                diagonal = false;
            }
        }
    }

    // Count the number of overlaps between lines
    let mut count = 0;
    for (_key, value) in &coordinates {
        if value > &1 {
            count += 1;
        }
    }

    println!("{}", count);  // Part 1 and 2
}

// Read lines util function
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}