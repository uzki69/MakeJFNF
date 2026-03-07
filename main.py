import os
import argparse
from pathlib import Path
import sys

def main():

    p = argparse.ArgumentParser("Links")
    p.add_argument("-i", "--input", required=True,  help="directory located files that will be linked", action='append', type=str)
    p.add_argument("output", help="directory where linked files will be", type=str)
    p.add_argument("title", help="tv show title", type=str)
    p.add_argument("season", help="tv show season", type=int)
    args = p.parse_args()

    filesToHandle: list[Path] = []

    if type(args.input) is list and type(args.output) is str and type(args.title) is str and type(args.season) is int:
        # append files to list
        for input_path in args.input:
            for entity in Path(input_path).iterdir(): 
                if entity.is_file():
                    filesToHandle.append(entity)
        
        # create episodes
        episode = 1
        outpath = Path(args.output)
        outpath = Path.joinpath(outpath, f"Season {args.season:02}")
        if not outpath.exists():
            outpath.mkdir(parents=True)
        for file in filesToHandle:
            create_link(file, outpath , args.title, args.season, episode)
            episode+=1
    else:
        print(f'input type error', sys.stderr)
def create_link(video: Path, out: Path, title: str, season: int, ep: int):
    if not video.name.endswith((".mkv", ".avi", ".mp4", ".webm", ".ts", ".ogg")):
        print(f"video type not supported: {video.name}", file=sys.stderr)
        return
    
    ext = video.name.split('.')[-1]
    
    name = f'{title} S{season:02}E{ep:02}.{ext}'
    
    linkTo = Path.joinpath(out, name)

    try:
        os.symlink(video.absolute(), linkTo.absolute())
    except Exception as e:
        print(f'error linking file: {e}', sys.stderr)


if __name__ == "__main__":
    main()
