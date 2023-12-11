extends Control

@onready var current_result = %current_result
@onready var previous_result = %previous_result

@export var current_result_value = 0
@export var previous_result_value = ""
# Called when the node enters the scene tree for the first time.
func _ready():
	_on_btn_ac_pressed()
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	pass
	
func InsertNum():
	pass

func AllClear():
	pass
	
	
func BackSpace():
	pass
	
func Calculate():
	pass

func _on_btn_ac_pressed():
	current_result.text = str(current_result_value)	
	previous_result.text = str(previous_result_value)	
	pass # Replace with function body.



func _on_btn_num_7_pressed():
	if(previous_result.text != ""):
		if(current_result.text == 0):
			current_result.text = str(7)
		else:
			current_result.text += str(7)
	pass # Replace with function body.
