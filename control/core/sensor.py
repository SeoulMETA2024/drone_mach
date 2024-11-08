import smbus
import time
import math

class KalmanFilter:
    def __init__(self, process_variance, measurement_variance, estimated_error, initial_value):
        self.process_variance = process_variance  # 프로세스 잡음
        self.measurement_variance = measurement_variance  # 측정 잡음
        self.estimated_error = estimated_error  # 추정 오차
        self.last_estimate = initial_value  # 이전 추정값

    def update_estimate(self, measurement):
        
        kalman_gain = self.estimated_error / (self.estimated_error + self.measurement_variance)
        
        current_estimate = self.last_estimate + kalman_gain * (measurement - self.last_estimate)
        
        self.estimated_error = (1 - kalman_gain) * self.estimated_error + abs(self.last_estimate - current_estimate) * self.process_variance
        
        self.last_estimate = current_estimate
        
        return current_estimate
        
class Sensor:
    def __init__(self, bus_number=1, sensor_address=0x68):
        self.bus = smbus.SMBus(bus_number)
        self.address = sensor_address
        self.init_sensor()

    def init_sensor(self):
        # MPU-6050 초기화 (파워 관리 레지스터 설정)
        self.bus.write_byte_data(self.address, 0x6B, 0x00)  # 파워 관리 레지스터 해제

    def read_raw_data(self, addr):
        # 센서에서 2바이트 데이터를 읽어온다
        high = self.bus.read_byte_data(self.address, addr)
        low = self.bus.read_byte_data(self.address, addr + 1)
        value = (high << 8) | low
        if value > 32768:
            value -= 65536
        return value

    def measure(self):
        # 자이로스코프 데이터 읽기
        gyro_x = self.read_raw_data(0x43)  # X축 자이로
        gyro_y = self.read_raw_data(0x45)  # Y축 자이로
        gyro_z = self.read_raw_data(0x47)  # Z축 자이로

        # 가속도계 데이터 읽기
        accel_x = self.read_raw_data(0x3B)  # X축 가속도
        accel_y = self.read_raw_data(0x3D)  # Y축 가속도
        accel_z = self.read_raw_data(0x3F)  # Z축 가속도

        # 자이로스코프 값을 각속도(dps, degrees per second)로 변환 (MPU-6050은 기본적으로 131 LSB/dps)
        gyro_x_dps = gyro_x / 131.0
        gyro_y_dps = gyro_y / 131.0
        gyro_z_dps = gyro_z / 131.0

        # 가속도 값을 중력(g) 단위로 변환 (MPU-6050은 기본적으로 16384 LSB/g)
        accel_x_g = accel_x / 16384.0
        accel_y_g = accel_y / 16384.0
        accel_z_g = accel_z / 16384.0

        return gyro_x_dps, gyro_y_dps, gyro_z_dps, accel_x_g, accel_y_g, accel_z_g

# # 칼만 필터 및 센서 사용 예제
# if __name__ == "__main__":
#     sensor = Sensor()
#     kalman_filter_gyro_x = KalmanFilter(process_variance=1, measurement_variance=4, estimated_error=2, initial_value=0)
#     kalman_filter_gyro_y = KalmanFilter(process_variance=1, measurement_variance=4, estimated_error=2, initial_value=0)
#     kalman_filter_gyro_z = KalmanFilter(process_variance=1, measurement_variance=4, estimated_error=2, initial_value=0)

#     while True:
#         # 센서로부터 자이로스코프와 가속도계 측정값 읽기
#         gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z = sensor.measure()
        
#         # 자이로스코프 값에 칼만 필터 적용
#         filtered_gyro_x = kalman_filter_gyro_x.update_estimate(gyro_x)
#         filtered_gyro_y = kalman_filter_gyro_y.update_estimate(gyro_y)
#         filtered_gyro_z = kalman_filter_gyro_z.update_estimate(gyro_z)

#         print(f"Filtered Gyro X: {filtered_gyro_x:.2f} dps, Filtered Gyro Y: {filtered_gyro_y:.2f} dps, Filtered Gyro Z: {filtered_gyro_z:.2f} dps")
#         print(f"Accel X: {accel_x:.2f} g, Accel Y: {accel_y:.2f} g, Accel Z: {accel_z:.2f} g")
        
#         time.sleep(0.1)
