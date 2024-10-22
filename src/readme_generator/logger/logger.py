from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

class Logger:
    def __init__(self):
        self.console = Console()
        self._verbose = False

    def set_verbose(self, value: bool) -> None:
        """Set verbose logging mode."""
        self._verbose = value

    def is_verbose(self) -> bool:
        """Check if verbose logging is enabled."""
        return self._verbose

    def get_progress(self) -> Progress:
        """Create and return a Progress instance with custom formatting."""
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        )

    def debug(self, message: str) -> None:
        """Log a debug message (only in verbose mode)."""
        if self._verbose:
            self.console.print(f"[dim blue]DEBUG: {message}[/]")

    def error(self, message: str, exc_info: bool = False) -> None:
        """Log an error message."""
        self.console.print(f"[red]Error: {message}[/]")
        if exc_info and self._verbose:
            import traceback
            self.console.print(f"[red]{traceback.format_exc()}[/]")

    def success(self, message: str) -> None:
        """Log a success message."""
        self.console.print(f"[green]{message}[/]")

    def warning(self, message: str) -> None:
        """Log a warning message."""
        self.console.print(f"[yellow]{message}[/]")

    def info(self, message: str) -> None:
        """Log an info message."""
        self.console.print(f"[cyan]{message}[/]")

    def log(self, *args, **kwargs) -> None:
        """Log a plain message."""
        self.console.print(*args, **kwargs)

    def trace(self, message: str) -> None:
        """Log a trace message (only in verbose mode)."""
        if self._verbose:
            self.console.print(f"[dim grey]TRACE: {message}[/]")

# Create and export a single global logger instance
logger = Logger()

# Export commonly used functions at module level
debug = logger.debug
error = logger.error
success = logger.success
warning = logger.warning
info = logger.info
log = logger.log
trace = logger.trace
get_progress = logger.get_progress
set_verbose = logger.set_verbose
is_verbose = logger.is_verbose