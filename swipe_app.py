import tkinter as tk

class PythonSwipeToChoose:
    def __init__(self, root):
        self.root = root
        self.root.title("Swipe To Choose (Python)")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f2f5")
        
        # Sample items to swipe through
        self.items = [
            {"text": "Python", "color": "#3776AB"},
            {"text": "JavaScript", "color": "#F7DF1E"},
            {"text": "Rust", "color": "#000000"},
            {"text": "Go Lang", "color": "#00ADD8"},
            {"text": "Swift", "color": "#FA4A0C"}
        ]
        self.current_index = 0
        
        # Track drag variables
        self.start_x = 0
        self.is_dragging = False
        self.swipe_threshold = 100 # Pixels needed to commit to a swipe
        
        # UI Setup
        self.create_widgets()
        self.load_next_card()

    def create_widgets(self):
        # Top Header Status
        self.status_label = tk.Label(
            self.root, text="Swipe Left to Dislike | Right to Like", 
            font=("Arial", 12), bg="#f0f2f5", fg="#555"
        )
        self.status_label.pack(pady=15)
        
        # The Card Canvas (Allows absolute widget placement/movement)
        self.canvas = tk.Canvas(self.root, width=300, height=350, bg="#f0f2f5", highlightthickness=0)
        self.canvas.pack(pady=10)
        
        # Visual Card Container
        self.card = tk.Frame(self.canvas, width=280, height=330, bg="white", highlightbackground="#ccc", highlightthickness=1)
        self.card.pack_propagate(False)
        self.card_id = self.canvas.create_window(150, 175, window=self.card) # Centered initially
        
        # Card Label
        self.card_label = tk.Label(self.card, text="", font=("Arial", 24, "bold"), bg="white")
        self.card_label.pack(expand=True)
        
        # Overlay Indicator (Shows LIKE / NOPE)
        self.overlay_label = tk.Label(self.card, text="", font=("Arial", 16, "bold"), bg="white")
        self.overlay_label.place(x=10, y=10)
        
        # Bind Mouse/Touch Gestures
        self.card.bind("<Button-1>", self.on_press)
        self.card_label.bind("<Button-1>", self.on_press)
        
        self.card.bind("<B1-Motion>", self.on_drag)
        self.card_label.bind("<B1-Motion>", self.on_drag)
        
        self.card.bind("<ButtonRelease-1>", self.on_release)
        self.card_label.bind("<ButtonRelease-1>", self.on_release)

    def load_next_card(self):
        self.overlay_label.config(text="")
        if self.current_index < len(self.items):
            item = self.items[self.current_index]
            self.card_label.config(text=item["text"], fg=item["color"])
            self.canvas.coords(self.card_id, 150, 175) # Reset card position to center
            self.is_dragging = False
        else:
            self.card_label.config(text="No More Cards!", fg="#888")
            self.overlay_label.config(text="")
            self.status_label.config(text="Finished!")

    def on_press(self, event):
        if self.current_index >= len(self.items):
            return
        self.start_x = event.x_root
        self.is_dragging = True

    def on_drag(self, event):
        if not self.is_dragging:
            return
        
        # Calculate horizontal distance dragged
        dx = event.x_root - self.start_x
        
        # Move the card visually on the canvas (Original Y remains centered at 175)
        new_x = 150 + dx
        self.canvas.coords(self.card_id, new_x, 175)
        
        # Live status updates/overlays as you drag
        if dx > 30:
            self.overlay_label.config(text="LIKE", fg="green")
        elif dx < -30:
            self.overlay_label.config(text="NOPE", fg="red")
        else:
            self.overlay_label.config(text="")

    def on_release(self, event):
        if not self.is_dragging:
            return
            
        dx = event.x_root - self.start_x
        
        # Determine outcome based on threshold
        if dx > self.swipe_threshold:
            self.animate_out(direction="right")
        elif dx < -self.swipe_threshold:
            self.animate_out(direction="left")
        else:
            # Snap Back to center
            self.snap_back()

    def animate_out(self, direction):
        # Trigger delegate action
        item_name = self.items[self.current_index]["text"]
        print(f"Card '{item_name}' was chosen with direction: {direction.upper()}")
        
        # Move to next card
        self.current_index += 1
        self.load_next_card()

    def snap_back(self):
        # Reset card position instantly back to center
        self.canvas.coords(self.card_id, 150, 175)
        self.overlay_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonSwipeToChoose(root)
    root.mainloop()
