class Config:

    def __init__(self):
        self.ORG_DATA_PATH = "dataset/preprocess"
        self.MM_ROWS_PATH  = "dataset/transform/rows_permutation"
        self.MM_COLS_PATH  = "dataset/transform/cols_permutation"
        self.Checkpoint    = "model/checkpoint"
        self.RLT_TRA_ROWS  = "result/transform/rows_permutation"
        self.RLT_TRA_COLS  = "result/transform/cols_permutation"
        self.UB_DATA_PATH  = "dataset/unbalanced"
        self.NE_DATA_PATH  = "dataset/nonequivalent"
