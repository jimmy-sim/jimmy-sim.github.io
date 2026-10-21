# -*- coding: utf-8 -*-
"""Stock price prediction comparison — original Colab code.

Requires all_stocks_5yr.csv in the working directory and NumPy, pandas,
Matplotlib, TensorFlow/Keras, and scikit-learn. Run sections in order.
This archived export includes no dataset, saved outputs, or version pins.
Only Colab's generated filename/link header has been replaced.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Store results from all models here so we can compare them at the very end
results = {}

# 1. Load and preprocess data
# Adjust the file path to match your environment (e.g. 'all_stocks_5yr.csv' or '../input/all_stocks_5yr.csv')
data = pd.read_csv('all_stocks_5yr.csv')

# If all_stocks_5yr.csv contains multiple tickers mixed together, extract just one ticker.
if 'Name' in data.columns:
    data = data[data['Name'] == 'GOOGL'].reset_index(drop=True)

# 2. Train / test split (80:20)
training_size = int(len(data) * 0.80)
data_len = len(data)

train = data.iloc[0:training_size]
test = data.iloc[training_size:data_len]

# Extract 'Open' price and normalize
train_open = train.loc[:, ["open"]].values

scaler = MinMaxScaler(feature_range=(0, 1))
train_scaled = scaler.fit_transform(train_open)

# 3. Build training time series data (timesteps)
timesteps = 40
X_train = []
y_train = []

for i in range(timesteps, len(train_scaled)):
    X_train.append(train_scaled[i - timesteps:i, 0])
    y_train.append(train_scaled[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# 4. Build and train the RNN model
model = keras.Sequential([
    keras.layers.SimpleRNN(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    keras.layers.Dropout(0.2),
    keras.layers.SimpleRNN(units=50, return_sequences=True),
    keras.layers.Dropout(0.2),
    keras.layers.SimpleRNN(units=50, return_sequences=True),
    keras.layers.Dropout(0.2),
    keras.layers.SimpleRNN(units=50),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(units=1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=100, batch_size=20)

# 5. Build test data and predict
# Prepend the previous `timesteps` (40 days) of data before the test set start to preserve continuity
dataset_total = data["open"]
inputs = dataset_total[len(dataset_total) - len(test) - timesteps:].values.reshape(-1, 1)
inputs = scaler.transform(inputs)

X_test = []
for i in range(timesteps, len(inputs)):
    X_test.append(inputs[i - timesteps:i, 0])

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Run prediction and inverse-transform back to the original scale
predict = model.predict(X_test)
predict = scaler.inverse_transform(predict)

# 6. Visualize results
real_price = test.loc[:, ["open"]].values

plt.figure(figsize=(10, 5))
plt.plot(real_price, color="red", label="Real Stock Price")
plt.plot(predict, color="black", label="Predicted Stock Price")
plt.title("Stock Price Prediction (RNN)")
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.legend()
plt.show()

# 7. Compute performance metrics (RMSE / MAE)
rnn_rmse = np.sqrt(mean_squared_error(real_price, predict))
rnn_mae = mean_absolute_error(real_price, predict)
results["RNN"] = {"RMSE": rnn_rmse, "MAE": rnn_mae}
print(f"[RNN] RMSE: {rnn_rmse:.4f}, MAE: {rnn_mae:.4f}")

# Naive baseline: "tomorrow's price = today's price", computed once here
naive_predict = dataset_total.shift(1).iloc[len(dataset_total) - len(test):].values.reshape(-1, 1)
naive_real = real_price
naive_rmse = np.sqrt(mean_squared_error(naive_real, naive_predict))
naive_mae = mean_absolute_error(naive_real, naive_predict)
results["Naive Baseline"] = {"RMSE": naive_rmse, "MAE": naive_mae}
print(f"[Naive Baseline] RMSE: {naive_rmse:.4f}, MAE: {naive_mae:.4f}")

"""2. LSTM"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

# 1. Load and preprocess data
# Adjust the CSV file path to match your environment (e.g. 'all_stocks_5yr.csv' or '../input/all_stocks_5yr.csv')
data = pd.read_csv('all_stocks_5yr.csv')

# Filter down to just the ticker you want (e.g. 'TSLA') from all_stocks_5yr.csv
if 'Name' in data.columns:
    data = data[data['Name'] == 'GOOGL'].reset_index(drop=True)

# 2. Train / test split (80:20)
training_size = int(len(data) * 0.80)
data_len = len(data)

train = data.iloc[0:training_size]
test = data.iloc[training_size:data_len]

# Extract 'Open' price and normalize
train_open = train.loc[:, ["open"]].values

scaler = MinMaxScaler(feature_range=(0, 1))
train_scaled = scaler.fit_transform(train_open)

# 3. Build training time series data (timesteps)
timesteps = 40
X_train = []
y_train = []

for i in range(timesteps, len(train_scaled)):
    X_train.append(train_scaled[i - timesteps:i, 0])
    y_train.append(train_scaled[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))


# ====================================================================
# 4. Build the model (LSTM)
# ====================================================================
model = keras.Sequential()

# First LSTM layer
model.add(keras.layers.LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(keras.layers.Dropout(0.2))

# Second LSTM layer
model.add(keras.layers.LSTM(units=50, return_sequences=True))
model.add(keras.layers.Dropout(0.2))

# Third LSTM layer
model.add(keras.layers.LSTM(units=50, return_sequences=True))
model.add(keras.layers.Dropout(0.2))

# Fourth LSTM layer
model.add(keras.layers.LSTM(units=50))
model.add(keras.layers.Dropout(0.2))

# Output layer
model.add(keras.layers.Dense(units=1))

model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=100, batch_size=20)
# ====================================================================


# 5. Build test data and predict
# Slice starting from (test set start - timesteps) across the full dataset to preserve continuity
dataset_total = data["open"]
inputs = dataset_total[len(dataset_total) - len(test) - timesteps:].values.reshape(-1, 1)
inputs = scaler.transform(inputs)

X_test = []
for i in range(timesteps, len(inputs)):
    X_test.append(inputs[i - timesteps:i, 0])

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Run prediction and inverse-transform back to the original scale
predict = model.predict(X_test)
predict = scaler.inverse_transform(predict)

# 6. Visualize results
real_price = test.loc[:, ["open"]].values

plt.figure(figsize=(10, 5))
plt.plot(real_price, color="red", label="Real Stock Price")
plt.plot(predict, color="black", label="Predicted Stock Price")
plt.title("Stock Price Prediction (LSTM)")
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.legend()
plt.show()

# 7. Compute performance metrics (RMSE / MAE)
lstm_rmse = np.sqrt(mean_squared_error(real_price, predict))
lstm_mae = mean_absolute_error(real_price, predict)
results["LSTM"] = {"RMSE": lstm_rmse, "MAE": lstm_mae}
print(f"[LSTM] RMSE: {lstm_rmse:.4f}, MAE: {lstm_mae:.4f}")

"""3. VAE"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler

# ====================================================================
# 1. Load and preprocess data
# ====================================================================
data = pd.read_csv('all_stocks_5yr.csv')

# Extract a specific ticker (e.g. 'AAPL')
if 'Name' in data.columns:
    data = data[data['Name'] == 'GOOGL'].reset_index(drop=True)

# Handle lowercase vs. capitalized column names
open_col = 'open' if 'open' in data.columns else 'Open'

training_size = int(len(data) * 0.80)
data_len = len(data)

train, test = data.iloc[0:training_size], data.iloc[training_size:data_len]

# Normalize the Open price
train_open = train.loc[:, [open_col]].values
scaler = MinMaxScaler(feature_range=(0, 1))
train_scaled = scaler.fit_transform(train_open)

timesteps = 40
end_len = len(train_scaled)
X_train = []
y_train = []

for i in range(timesteps, end_len):
    X_train.append(train_scaled[i - timesteps:i, 0])
    y_train.append(train_scaled[i, 0])  # Tomorrow's price (target)

X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
y_train = np.reshape(y_train, (y_train.shape[0], 1))

# ====================================================================
# 2. Define VAE forecasting model components
# ====================================================================
latent_dim = 4  # Latent dimension raised to 4 for more representational capacity

# (1) Sampling layer
class Sampling(layers.Layer):
    def call(self, inputs):
        z_mean, z_log_var = inputs
        batch = tf.shape(z_mean)[0]
        dim = tf.shape(z_mean)[1]
        epsilon = tf.random.normal(shape=(batch, dim))
        return z_mean + tf.exp(0.5 * z_log_var) * epsilon

# (2) Encoder: past 40-day sequence -> compressed into latent space
encoder_inputs = layers.Input(shape=(timesteps, 1))
x = layers.LSTM(64, return_sequences=True)(encoder_inputs)
x = layers.Dropout(0.2)(x)
x = layers.LSTM(32)(x)
x = layers.Dropout(0.2)(x)

z_mean = layers.Dense(latent_dim, name="z_mean")(x)
z_log_var = layers.Dense(latent_dim, name="z_log_var")(x)
z = Sampling()([z_mean, z_log_var])
encoder = keras.Model(encoder_inputs, [z_mean, z_log_var, z], name="encoder")

# (3) Decoder: latent space -> a single next-day price (point prediction)
latent_inputs = layers.Input(shape=(latent_dim,))
x = layers.Dense(32, activation="relu")(latent_inputs)
x = layers.Dropout(0.2)(x)
x = layers.Dense(16, activation="relu")(x)
decoder_outputs = layers.Dense(1)(x)  # Predicted next-day price
decoder = keras.Model(latent_inputs, decoder_outputs, name="decoder")

# (4) VAE forecasting class with a custom train_step
class VAEForecaster(keras.Model):
    def __init__(self, encoder, decoder, kl_weight=0.001, **kwargs):
        super().__init__(**kwargs)
        self.encoder = encoder
        self.decoder = decoder
        self.kl_weight = kl_weight  # Weight to prevent the KL loss from dominating training
        self.total_loss_tracker = keras.metrics.Mean(name="total_loss")
        self.pred_loss_tracker = keras.metrics.Mean(name="pred_loss")
        self.kl_loss_tracker = keras.metrics.Mean(name="kl_loss")

    @property
    def metrics(self):
        return [self.total_loss_tracker, self.pred_loss_tracker, self.kl_loss_tracker]

    def train_step(self, data):
        x_input, y_target = data  # Split into input (past 40 days) and target (next-day price)

        with tf.GradientTape() as tape:
            z_mean, z_log_var, z = self.encoder(x_input)
            y_pred = self.decoder(z)

            # 1. Prediction loss (MSE)
            pred_loss = tf.reduce_mean(tf.square(y_target - y_pred))

            # 2. KL divergence loss
            kl_loss = -0.5 * tf.reduce_mean(
                tf.reduce_sum(1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var), axis=-1)
            )

            # Total loss = prediction loss + weighted KL loss
            total_loss = pred_loss + (self.kl_weight * kl_loss)

        grads = tape.gradient(total_loss, self.trainable_weights)
        self.optimizer.apply_gradients(zip(grads, self.trainable_weights))

        self.total_loss_tracker.update_state(total_loss)
        self.pred_loss_tracker.update_state(pred_loss)
        self.kl_loss_tracker.update_state(kl_loss)
        return {
            "loss": self.total_loss_tracker.result(),
            "pred_loss": self.pred_loss_tracker.result(),
            "kl_loss": self.kl_loss_tracker.result(),
        }

# ====================================================================
# 3. Train the model
# ====================================================================
vae_model = VAEForecaster(encoder, decoder, kl_weight=0.001)
vae_model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001))

# Pass X_train (past 40 days) and y_train (next-day price) together for training
vae_model.fit(X_train, y_train, epochs=100, batch_size=20)

# ====================================================================
# 4. Build test data and predict
# ====================================================================
dataset_total = data[open_col]
inputs = dataset_total[len(dataset_total) - len(test) - timesteps:].values.reshape(-1, 1)
inputs = scaler.transform(inputs)

X_test = []
for i in range(timesteps, len(inputs)):
    X_test.append(inputs[i - timesteps:i, 0])

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Encoder -> extract z_mean -> pass through Decoder to predict
z_mean_test, _, _ = vae_model.encoder.predict(X_test)
predict = vae_model.decoder.predict(z_mean_test)

# Inverse-transform back to the original scale
predict = scaler.inverse_transform(predict)

# ====================================================================
# 5. Visualize
# ====================================================================
real_price = test.loc[:, [open_col]].values

plt.figure(figsize=(12, 6))
plt.plot(real_price, color="red", label="Real Stock Price")
plt.plot(predict, color="black", label="Predicted Stock Price (VAE)")
plt.title("Stock Price Prediction (VAE)")
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.legend()
plt.grid(True)
plt.show()

# 6. Compute performance metrics (RMSE / MAE)
vae_rmse = np.sqrt(mean_squared_error(real_price, predict))
vae_mae = mean_absolute_error(real_price, predict)
results["VAE"] = {"RMSE": vae_rmse, "MAE": vae_mae}
print(f"[VAE] RMSE: {vae_rmse:.4f}, MAE: {vae_mae:.4f}")

# ====================================================================
# 7. Compare all models (RNN vs LSTM vs VAE vs Naive Baseline)
# ====================================================================
comparison_df = pd.DataFrame(results).T
comparison_df = comparison_df.sort_values("RMSE")
print("\n=== Model Comparison (lower is better) ===")
print(comparison_df)

comparison_df["RMSE"].plot(kind="bar", figsize=(8, 5), title="RMSE by Model (lower is better)")
plt.ylabel("RMSE")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()