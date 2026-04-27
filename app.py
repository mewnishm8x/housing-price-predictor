{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "6fe4602c-cf34-48dc-b411-9a299e21b3f8",
      "cell_type": "code",
      "source": "import streamlit as st\nimport pickle\nimport numpy as np\n\n# Load model\nmodel = pickle.load(open(\"model.pkl\", \"rb\"))\n\nst.title(\"🏠 Housing Price Predictor\")\n\nst.write(\"Enter house details to estimate price:\")\n\n# Inputs\narea = st.number_input(\"Area (sq ft)\", 500, 10000, 1500)\nbedrooms = st.slider(\"Bedrooms\", 1, 10, 3)\nbathrooms = st.slider(\"Bathrooms\", 1, 10, 2)\nstories = st.slider(\"Stories\", 1, 5, 1)\n\nmainroad = st.selectbox(\"Main Road Access\", [\"Yes\", \"No\"])\nfurnishing = st.selectbox(\"Furnishing Status\", [\"Furnished\", \"Semi-Furnished\", \"Unfurnished\"])\n\n# Encoding\nmainroad_val = 1 if mainroad == \"Yes\" else 0\nfurnishing_map = {\"Furnished\": 2, \"Semi-Furnished\": 1, \"Unfurnished\": 0}\nfurnishing_val = furnishing_map[furnishing]\n\n# Predict\nif st.button(\"Predict Price\"):\n    features = np.array([[area, bedrooms, bathrooms, stories, mainroad_val, furnishing_val]])\n    prediction = model.predict(features)[0]\n\n    st.subheader(f\"💰 Estimated Price: ${prediction:,.2f}\")\n\n    # Extra insight\n    if prediction > 500000:\n        st.success(\"🏡 High-value property\")\n    elif prediction > 200000:\n        st.warning(\"🏠 Mid-range property\")\n    else:\n        st.info(\"🏚️ Budget property\")",
      "metadata": {
        "trusted": True
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}
