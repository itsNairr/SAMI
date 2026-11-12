# SAMI

SAMI (Sidewalk Accessibility Monitoring and Inspection) is a Queen's University
capstone project to develop a robot that identifies sidewalk accessibility hazards.
This repository contains the project documents, design files, and test records.

## Navigation

| Document | Contents |
| --- | --- |
| [Project proposal](./deliverables/Capstone%20Group%203%20Project%20Proposal.docx) | Project purpose, scope, requirements, objectives, and schedule. |
| [City of Kingston presentation](./deliverables/City%20of%20Kingston%20Presentation.pptx) | Presentation for the City of Kingston. |
| [SAMI storyboard](./Deliverables/Storyboard%20of%20SAMI.pdf) | Project storyboard. |
| [Risk register](./Deliverables/SAMIRiskRegister.xlsx) | Project risk records. |
| [Group tasks](./deliverables/Group%20Tasks.xlsx) | Team task records. |
| [Timesheet](./Deliverables/Timesheet.xlsx) | Team time records. |
| [Archived proposals](./deliverables/Archive/) | Earlier proposal copies and backups. |

## Design files

| Folder | Contents |
| --- | --- |
| [Mechanical design](./Design/Mechanical/) | Robot and sensor CAD files, initial configuration drawing, and calculations. |
| [Electrical design](./Design/Electrical/) | Power distribution diagram and LiDAR and laptop buck converter calculations. |
| [Branding](./design/Branding/) | SAMI logo files. |

## Test records

| System | Records |
| --- | --- |
| [Camera](./Testing/Individual%20System/Camera/) | Depth test notes and drawing. |
| [Husky base](./Testing/Individual%20System/HuskyBase/) | ROS commands and connection notes. |
| [IMU](./Testing/Individual%20System/IMU/) | MicroStrain IMU test records. |
| [LiDAR](./Testing/Individual%20System/LiDAR/) | SICK LiDAR test notes. |
| [Simulation](./Testing/Individual%20System/Simulation/) | Simulation records. |
| [YOLO crack detection](./Testing/Individual%20System/YOLOCrackDetection/) | Training notes, test script, trained model, and result files. |
| [Collision avoidance](./Testing/Subsytems/Collision%20avoidance/) | Subsystem test document and recorded data. |

## Project notes

- [Client meetings](./Notes/ClientMeetings/): meeting records.
- [Tasks completed](./notes/Tasks%20Completed.docx): completed work records.
- [Week 2 goals](./notes/Goals%20Week%202.docx): early project goals.

## Code

The ROS 2 workspace, simulation, and sensor utilities are maintained in the
[SAMI_code repository](https://github.com/itsNairr/SAMI_code).

See that repository's README for setup, build, and launch instructions.

## Local data

The local `Data/` folder contains data archives. It is excluded from Git by
[.gitignore](./.gitignore), so these archives are not included in the repository.

## AI use and reference

ChatGPT (OpenAI, n.d.) was used to organize and draft this README from the
repository contents. This statement applies to README creation.

OpenAI. (n.d.). *ChatGPT* [Large language model]. Retrieved November 12, 2026,
from https://chatgpt.com/
