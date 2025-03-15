Mastering Filesystem Hierarchy and Links in Linux! 🚀

🔍 Building a Foundation for Efficient File Management and System Organization!
This project focused on mastering the Linux filesystem hierarchy and the creation of hard and soft (symbolic) links, empowering me to navigate key directories, manage file access points, and centralize configurations. Key skills and accomplishments include:

🔑 Filesystem Hierarchy Exploration:
Navigated the root directory and explored essential system directories using ls / and ls /bin /etc /home /var /usr. This provided insights into directory structures and their purposes, like binaries in /bin, configurations in /etc, and user files in /home.
🔗 Hard Link Creation:
Created hard links pointing to the same inode, ensuring redundant file access using ln source_file hard_link. For example, ln example.txt example_hard.txt allowed data redundancy while maintaining minimal storage overhead.
🔗 Soft (Symbolic) Link Creation:
Created flexible soft links pointing to file paths, enabling centralized configuration and easy redirection using ln -s source_file soft_link. For example, ln -s example.txt example_soft.txt effectively linked to the source file.
✅ Verification and Link Management:
Verified links and their targets using ls -l, ensuring proper linking and permissions.
Removed unwanted links safely using rm link_name, maintaining an organized filesystem.
