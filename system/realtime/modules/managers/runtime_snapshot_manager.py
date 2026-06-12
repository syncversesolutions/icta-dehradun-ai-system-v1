import json
import shutil
from datetime import datetime
from pathlib import Path
from config.paths import BASE_DIR
class RuntimeSnapshotManager:
    def __init__(self):
        # ====================================
        # PROJECT ROOT
        # ====================================
        self.base_dir = (
            Path(BASE_DIR)
        )
        # ====================================
        # RUNTIME ROOT
        # ====================================
        self.runtime_root = (
            self.base_dir /
            "runtime"
        )
        # ====================================
        # SNAPSHOT ROOT
        # ====================================
        self.snapshot_root = (
            self.runtime_root /
            "snapshots"
        )
        # ====================================
        # SYSTEM STATE
        # ====================================
        self.system_state_path = (
            self.base_dir /
            "system/state/system_state.json"
        )
        # ====================================
        # PROCESSED DATA
        # ====================================
        self.processed_root = (
            self.base_dir /
            "data/processed"
        )
    # ========================================
    # CREATE SNAPSHOT
    # ========================================
    def create_snapshot(self):
        # ====================================
        # TIMESTAMP
        # ====================================
        timestamp = datetime.now().strftime(
            "%Y_%m_%d_%H%M%S"
        )
        snapshot_name = (
            f"snapshot_{timestamp}"
        )
        snapshot_path = (
            self.snapshot_root /
            snapshot_name
        )
        # ====================================
        # CREATE DIRECTORY
        # ====================================
        snapshot_path.mkdir(
            parents=True,
            exist_ok=True
        )
        # ====================================
        # COPY SYSTEM STATE
        # ====================================
        if self.system_state_path.exists():
            shutil.copy(
                self.system_state_path,
                snapshot_path /
                "system_state.json"
            )
        # ====================================
        # COPY ARTIFACTS
        # ====================================
        if self.processed_root.exists():
            for artifact in (
                self.processed_root.iterdir()
            ):
                if artifact.is_file():
                    shutil.copy(
                        artifact,
                        snapshot_path /
                        artifact.name
                    )
        # ====================================
        # SNAPSHOT METADATA
        # ====================================
        metadata = {
            "snapshot_name":
                snapshot_name,
            "created_at":
                timestamp,
            "source":
                "ICTA Runtime",
            "state_file":
                "system_state.json"
        }
        # ====================================
        # SAVE METADATA
        # ====================================
        with open(
            snapshot_path /
            "metadata.json",
            "w"
        ) as f:
            json.dump(
                metadata,
                f,
                indent=4
            )
        print("\n")
        print("=" * 60)
        print(
            "RUNTIME SNAPSHOT CREATED ✅"
        )
        print(snapshot_name)
        print(snapshot_path)
        print("=" * 60)
        return snapshot_path
    # ========================================
    # LIST SNAPSHOTS
    # ========================================
    def list_snapshots(self):
        snapshots = []
        if not self.snapshot_root.exists():
            return snapshots
        for snapshot in (
            self.snapshot_root.iterdir()
        ):
            if snapshot.is_dir():
                snapshots.append(
                    snapshot.name
                )
        return sorted(snapshots)
    # ========================================
    # LOAD SNAPSHOT
    # ========================================
    def load_snapshot(
        self,
        snapshot_name
    ):
        snapshot_path = (
            self.snapshot_root /
            snapshot_name
        )
        state_path = (
            snapshot_path /
            "system_state.json"
        )
        if not state_path.exists():
            print(
                "\nSnapshot state not found"
            )
            return None
        with open(
            state_path,
            "r"
        ) as f:
            state = json.load(f)
        return state