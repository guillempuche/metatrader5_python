#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de ejemplo para conectarse a MetaTrader 5, obtener datos y calcular un indicador.
"""

from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()


MT5_PATH   = os.getenv("MT5_PATH") # Ruta del programa MetaTrader 5
LOGIN      = int(os.getenv("LOGIN", "0")) # Número de cuenta
PASSWORD   = os.getenv("PASSWORD") # Contraseña
SERVER     = os.getenv("SERVER") # Servidor
TIMEOUT_MS = int(os.getenv("TIMEOUT_MS", "60000")) # Timeout en milisegundos
SYMBOL      = "EURUSD" # Símbolo
TIMEFRAME   = mt5.TIMEFRAME_M15  # Tiempoframe
NUM_BARS    = 100

def connect_mt5(path=None, login=None, password=None, server=None, timeout=60000):
    """Inicializa MT5 y hace login en la cuenta especificada."""
    # Inicializar MT5 (busca terminal.exe si path es None)
    if not mt5.initialize(path, login=login, password=password, server=server, timeout=timeout):
        print(f"[ERROR] initialize() fallo, código: {mt5.last_error()}")
        return False

    # Opcional: comprobar información del terminal
    info = mt5.terminal_info()
    print("Conectado al terminal:", info.name, info.company)
    print("Versión MT5:", mt5.version())

    # Verificar que estamos autorizados en la cuenta
    # (si initialize() lleva login, este paso puede no ser necesario)
    authorized = mt5.login(login, password=password, server=server, timeout=timeout)
    if not authorized:
        print(f"[ERROR] login() fallo en cuenta #{login}, código: {mt5.last_error()}")
        mt5.shutdown()
        return False

    print(f"[OK] Sesión iniciada en cuenta #{login} en servidor '{server}'")
    return True

def disconnect_mt5():
    """Cierra la conexión con MT5."""
    mt5.shutdown()
    print("[OK] Conexión MT5 cerrada.")

def get_rates(symbol, timeframe, n_bars):
    """Obtiene n_bars de barras OHLC y las devuelve como DataFrame."""
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n_bars)
    if rates is None or len(rates) == 0:
        print(f"[ERROR] No se han obtenido datos para {symbol}")
        return None
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def calculate_rsi(series, period=14):
    """Calcula el RSI de una serie de precios."""
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def main():
    if not connect_mt5(path=MT5_PATH, login=LOGIN, password=PASSWORD, server=SERVER, timeout=TIMEOUT_MS):
        return

    # 1) Obtener datos
    df = get_rates(SYMBOL, TIMEFRAME, NUM_BARS)
    if df is None:
        disconnect_mt5()
        return

    # 2) Calcular RSI
    df['rsi'] = calculate_rsi(df['close'], period=14)

    # 3) Evaluar señal sencilla
    ultima_rsi = df['rsi'].iloc[-1]
    print(f"RSI actual de {SYMBOL}: {ultima_rsi:.2f}")
    if ultima_rsi < 30:
        print(" → Sobreventa (posible señal de COMPRA).")
    elif ultima_rsi > 70:
        print(" → Sobrecompra (posible señal de VENTA).")
    else:
        print(" → Mercado neutral.")

    # 4) (Opcional) Mostrar las últimas filas
    print(df[['time','open','high','low','close','rsi']].tail(5))

    # 5) Desconectar
    disconnect_mt5()

if __name__ == "__main__":
    main()