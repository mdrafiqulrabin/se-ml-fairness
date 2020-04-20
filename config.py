class Config:

    def __init__(self):
        self.RS = 42
        self.ORG_DATA_PATH = "dataset/preprocess"
        self.MM_ROWS_PATH  = "dataset/transform/rows_permutation"
        self.MM_COLS_PATH  = "dataset/transform/cols_permutation"
        self.UB_DATA_PATH  = "dataset/unbalanced"
        self.NE_DATA_PATH  = "dataset/nonequivalent"
        self.MODEL_CKPOINT = "result/checkpoint"
        self.RLT_PER_ROWS  = "result/transform/rows_permutation"
        self.RLT_PER_COLS  = "result/transform/cols_permutation"
        self.RLT_UB_DATA   = "result/unbalanced"
        self.RLT_NE_DATA   = "result/nonequivalent"
