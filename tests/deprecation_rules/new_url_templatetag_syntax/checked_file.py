# Old style url
<form action="{% url myview %}" method="POST">
# New style
<form action="{% url 'myview' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="Submit"/>
</form>
