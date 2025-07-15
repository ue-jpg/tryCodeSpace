def main():
    # ファイル名の定義
    input_file = "seiseki.txt"
    output_file = "seiseki_totave.txt"
    
    # データを格納するリスト
    students = []
    
    # ファイルを読み込み
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"エラー: {input_file} が見つかりません")
        return
    
    # ヘッダー行をスキップして、データを解析
    header = lines[0].strip()
    
    for line in lines[1:]:  # 1行目（ヘッダー）をスキップ
        line = line.strip()
        if not line:  # 空行をスキップ
            continue
            
        # データを分割
        parts = line.split()
        if len(parts) >= 4:
            student_id = parts[0]  # (1), (2), ...
            math_score = int(parts[1])
            eng_score = int(parts[2])
            jpn_score = int(parts[3])
            
            # 合計点と平均点を計算
            total = math_score + eng_score + jpn_score
            average = total / 3.0
            
            students.append({
                'id': student_id,
                'math': math_score,
                'eng': eng_score,
                'jpn': jpn_score,
                'total': total,
                'average': average
            })
    
    # 各教科の平均点を計算
    if students:
        math_sum = sum(student['math'] for student in students)
        eng_sum = sum(student['eng'] for student in students)
        jpn_sum = sum(student['jpn'] for student in students)
        num_students = len(students)
        
        math_avg = math_sum / num_students
        eng_avg = eng_sum / num_students
        jpn_avg = jpn_sum / num_students
    else:
        math_avg = eng_avg = jpn_avg = 0
    
    # 結果をファイルに出力
    with open(output_file, 'w', encoding='utf-8') as f:
        # ヘッダーを出力
        f.write(header + '\n')
        
        # 各生徒のデータを出力
        for student in students:
            f.write(f"{student['id']} {student['math']:3d} {student['eng']:3d} {student['jpn']:3d} = {student['total']:3d}({student['average']:.1f})\n")
        
        # 区切り線
        f.write("-------------------------\n")
        
        # 各教科の平均点を出力
        f.write(f"ave: {math_avg:.1f} {eng_avg:.1f} {jpn_avg:.1f}\n")
    
    print(f"処理完了: {output_file} に結果を出力しました")
    print(f"処理した学生数: {len(students)}人")

if __name__ == "__main__":
    main()
