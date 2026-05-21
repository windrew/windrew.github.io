import re
import sys
from pathlib import Path

def sort_problems(file_path):
    path = Path(file_path)
    if not path.exists():
        print(f"File {file_path} not found.")
        return

    content = path.read_text(encoding='utf-8')
    lines = content.splitlines()

    # Identify the problem list lines
    # Pattern: [Div.2 813D](https://...) (2000)
    problem_pattern = re.compile(r'^\[(.*?)\]\(.*?\)\s*\((\d+)\)\s*$')
    
    start_index = -1
    end_index = -1
    problem_lines = []

    for i, line in enumerate(lines):
        if problem_pattern.match(line):
            if start_index == -1:
                start_index = i
            end_index = i
            problem_lines.append(line)
        elif start_index != -1 and not line.strip():
            # Stop at the first empty line after the list starts
            # But wait, there might be multiple lists? 
            # For now, assume it's one contiguous block or multiple blocks separated by something.
            # Let's just collect all matches and their indices.
            pass

    if not problem_lines:
        print("No problem list found.")
        return

    # We need to handle non-contiguous blocks if they exist, 
    # but the user likely wants to sort the whole list.
    # Let's find all contiguous blocks and sort each, OR sort all and put them back.
    # Given the user's request, they likely want one sorted list.
    
    # Let's refine: find the range where problems are.
    # Re-scanning to find the exact range(s)
    blocks = []
    current_block = []
    
    for i, line in enumerate(lines):
        if problem_pattern.match(line):
            if not current_block:
                current_start = i
            current_block.append((i, line))
        else:
            if current_block:
                blocks.append((current_start, i - 1, current_block))
                current_block = []
    if current_block:
        blocks.append((current_start, len(lines) - 1, current_block))

    if not blocks:
        return

    # For now, let's just sort each block individually if they are separate.
    # Or merge them? The user's file has them together.
    
    new_lines = list(lines)
    
    for start, end, block in blocks:
        # block is a list of (index, line)
        
        def sort_key(item):
            line = item[1]
            match = problem_pattern.match(line)
            if not match:
                return (0, 0, "")
            
            display_text = match.group(1) # e.g. "Div.2 813D"
            rating = int(match.group(2))
            
            # Extract round number from display text
            # e.g. "Div.2 813D" -> 813
            round_match = re.search(r'(\d+)', display_text)
            round_num = int(round_match.group(1)) if round_match else 0
            
            # Extract problem index e.g. "D"
            prob_index = display_text.split()[-1]
            # remove digits from prob_index to get just the letters? 
            # 1089C2 -> C2
            prob_id = re.sub(r'^\d+', '', prob_index)
            
            # Sort Key: 
            # 1. Rating ASC
            # 2. Round number DESC (user said "라운드 내림차순")
            # 3. Prob ID ASC (implied)
            return (rating, -round_num, prob_id)

        sorted_block = sorted(block, key=sort_key)
        
        # Replace the lines in the file
        for i, (orig_idx, _) in enumerate(block):
            new_lines[orig_idx] = sorted_block[i][1]

    path.write_text('\n'.join(new_lines) + '\n', encoding='utf-8')
    print(f"Successfully sorted problems in {file_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for file_path in sys.argv[1:]:
            sort_problems(file_path)
    else:
        # Default to the known file
        sort_problems("_posts/2026-05-21-valuable_problems.markdown")
