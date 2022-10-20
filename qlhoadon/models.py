from logging.config import stopListening
from django.db import models

# Create your models here.

class DonVi(models.Model):
    MaSoThue = models.CharField(max_length=14)
    TenDonVi = models.CharField(max_length=255)
    DiaChi = models.CharField(max_length=255)
    SoDienThoai = models.CharField(max_length=20)
    


class HoaDonDienTu(models.Model):
    
    MaSoThue = models.CharField(max_length=14)
    KyHieu = models.CharField(max_length=255)
    So = models.CharField(max_length=255)
    NgayHoaDon = models.DateField()
    SoTien = models.BigIntegerField()
    DiaChiTraCuu = models.CharField(max_length=255)
    MaSoBiMat = models.CharField(max_length=255)    
    NguoiThanhToan  = models.CharField(max_length=255)
    NgayNhap =models.DateField()    
    DaThanhToan = models.BooleanField()
    NgayThanhToan = models.DateField()
    

