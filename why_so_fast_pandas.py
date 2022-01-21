import perfplot
import pandas as pd

def vec(df):
    return df['A'] + df['B']

def vec_numpy(df):
    return df['A'].to_numpy() + df['B'].to_numpy()

def list_comp(df):
    return [x + y for x, y in zip(df['A'], df['B'])]

def apply(df):
    return df.apply(lambda row: row['A'] + row['B'], axis=1)

def iterrows(df):
    result = []
    for index, row in df.iterrows():
        result.append(row['A'] + row['B'])

    return result


df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
kernels = [vec, vec_numpy, list_comp, apply, iterrows]

perfplot.show(
    setup=lambda n: pd.concat([df] * n, ignore_index=True),
    kernels=kernels,
    labels=[str(k.__name__) for k in kernels],
    n_range=[2**k for k in range(16)],
    xlabel='N',
    logx=True,
    logy=True)