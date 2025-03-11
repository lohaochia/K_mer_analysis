import pandas as pd
###列出兩性別比較特異性kmer總類
# 读取两个文件的数据
f2_kmers_df = pd.read_csv('/work/u1432917/F4_AG_kmers.txt', sep=' ', names=['kmer', 'count'])
m2_kmers_df = pd.read_csv('/work/u1432917/M4_AG_kmers.txt', sep=' ', names=['kmer', 'count'])

# 将数据转换为字典以便快速查找
f2_kmers_dict = dict(zip(f2_kmers_df['kmer'], f2_kmers_df['count']))
m2_kmers_dict = dict(zip(m2_kmers_df['kmer'], m2_kmers_df['count']))

# 找出两个文件中相同和不同的 k-mer
f2_kmers_set = set(f2_kmers_dict.keys())
m2_kmers_set = set(m2_kmers_dict.keys())

common_kmers = f2_kmers_set & m2_kmers_set
f2_unique_kmers = f2_kmers_set - common_kmers
m2_unique_kmers = m2_kmers_set - common_kmers

# 筛选出出现次数在 20 次到 2000 次之间的特异性 k-mer
f2_filtered_kmers = {kmer: count for kmer, count in f2_kmers_dict.items() if kmer in f2_unique_kmers and 22 <= count <= 2000}
m2_filtered_kmers = {kmer: count for kmer, count in m2_kmers_dict.items() if kmer in m2_unique_kmers and 19 <= count <= 2000}

# 将结果转换为 DataFrame
f2_filtered_kmers_df = pd.DataFrame(f2_filtered_kmers.items(), columns=['kmer', 'count'])
m2_filtered_kmers_df = pd.DataFrame(m2_filtered_kmers.items(), columns=['kmer', 'count'])

# 输出结果到 TXT 文件
f2_output_file = '/work/u1432917/F4_unique_filtered_kmers.txt'
m2_output_file = '/work/u1432917/M4_unique_filtered_kmers.txt'

f2_filtered_kmers_df.to_csv(f2_output_file, sep=' ', index=False, header=False)
m2_filtered_kmers_df.to_csv(m2_output_file, sep=' ', index=False, header=False)

print(f'F2 unique filtered kmers have been written to {f2_output_file}')
print(f'M2 unique filtered kmers have been written to {m2_output_file}')
