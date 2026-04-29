## This application make links to videos for the jellyfin shows format

### Like:
```
input: 
 Series Name S1 - [HEVC] - '2014' Special Edition 
  ├──  [HEVC] A File name that doesn't work properly
  ├──  [HEVC] B Another File With wrong name
  ├──  [HEVC] C Another File With wrong name
  └──  [HEVC] D nother File With wrong name
output:
 Season 01
  ├── Series Name A S01E01.mkv
  ├── Series Name A S01E02.mkv
  ├── Series Name A S01E03.mkv
  └── Series Name A S01E04.mkv
  ```

## How to use (Linux)

```sh
export in=/path/to/series
export out=/output/path

## Series/season 1
./main.py -i "$in/some-random-bs-seasonssj1" "$out/seriesname" "series name"  1

## Series + extras that's together in IMDB 
./main.py -i "$in/season1" -i "$in/extras"  "$out/seriesname"  "series name" 1
```

## Arch Linux
```sh
yay make-jfnf
```
Or
```sh
git clone https://github.com/uzki69/MakeJFNF.git
cd MakeJFNF
makepkg -si
```
