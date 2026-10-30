import pickle

import pandas as pd

from domain.domain import GHRInput, GHRPredicationResponse


class GHRService:

    def __init__(self):
        self.path_model = "artifacts/XGB_best_model.pkl"
        self.model = self.load_artifacts(self.path_model)

    def load_artifacts(self, path_to_artifacts):
        """Load artifacts from a pickle file."""
        with open(path_to_artifacts, "rb") as f:
            artifacts = pickle.load(f)

        return artifacts

    def preprocess_input(self, request: GHRInput) -> pd.DataFrame:
        data_dict = {
            "P": request.P,
            "RH": request.RH,
            "SH": request.SH,
            "MaxTem": request.MaxTem,
            "MinTem": request.MinTem,
            "TemR": request.TemR,
            "WS": request.WS,
        }

        data_df = pd.DataFrame.from_dict([data_dict])

        return data_df

    def predict_GHR(self, request: GHRInput) -> GHRPredicationResponse:

        input_df = self.preprocess_input(request)

        GHR_prediction = self.model.predict(input_df)[0]

        GHR_prediction = float(GHR_prediction)

        return GHRPredicationResponse(H=GHR_prediction)

# if __name__ == "__main__":
#     test_request = GHRInput(P=1013.25, RH=50.0, SH=10.0, MaxTem=30.0, MinTem=20.0, TemR=25.0, WS=5.0)
#     GHR_serv = GHRService()
#     result = GHR_serv.predict_GHR(request=test_request)
#     print(result.GHResult)
