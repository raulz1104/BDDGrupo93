from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    calificacion_media = models.FloatField()

class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)

class Delivery(models.Model):
    nombre = models.CharField(max_length=200)
    precio_servicio = models.IntegerField()
    precio_suscripcion = models.IntegerField()
    calificacion_media = models.FloatField()

class Suscriptor(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    medio = models.CharField(max_length=200)
    prox_pago = models.CharField(max_length=200)
    ciclo = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cliente', 'delivery'], name='unique_cliente_delivery')
        ]

class Restaurant(models.Model):
    nombre = models.CharField(max_length=200)
    vigente = models.CharField(max_length=200)

class Sucursal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)

class Despachador(models.Model):
    telefono = models.CharField(max_length=200, primary_key=True)
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    calificacion_media = models.FloatField()

class DeliverySucursal(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

class DespachadorDelivery(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    despachador = models.ForeignKey(Despachador, on_delete=models.CASCADE)

class DespachadorDeliveryPropio(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class DespachadorDetalles(models.Model):
    despachador = models.ForeignKey(Despachador, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Plato(models.Model):
    restaurante = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    disponibilidad = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    tamaño = models.CharField(max_length=200)
    personas_porcion = models.CharField(max_length=200)
    precio_plato = models.CharField(max_length=200)
    t_preparacion = models.CharField(max_length=200)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=200)
    hora = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)

class PedidoRealizado(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    evaluacion_cliente = models.FloatField()
    evaluacion_despacho = models.FloatField()

class PlatoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Despacho(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    costo = models.IntegerField()
    tiempo = models.CharField(max_length=200)

class ServicioDespachoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    despachador = models.ForeignKey(Despachador, on_delete=models.CASCADE)

class ServicioDespachoInfo(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
