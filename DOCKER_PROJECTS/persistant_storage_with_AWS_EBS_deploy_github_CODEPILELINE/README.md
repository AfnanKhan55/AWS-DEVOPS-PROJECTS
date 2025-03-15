𝘗𝘦𝘳𝘴𝘪𝘴𝘵𝘦𝘯𝘵 𝘋𝘰𝘤𝘬𝘦𝘳 𝘚𝘵𝘰𝘳𝘢𝘨𝘦 𝘸𝘪𝘵𝘩 𝐀𝐖𝐒 𝐄𝐁𝐒 & 𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐞𝐝 𝐃𝐞𝐩𝐥𝐨𝐲𝐦𝐞𝐧𝐭 𝐯𝐢𝐚 𝐆𝐢𝐭𝐇𝐮𝐛 & 𝐀𝐖𝐒 𝐂𝐨𝐝𝐞𝐏𝐢𝐩𝐞𝐥𝐢𝐧𝐞!⁣
⁣
📌 ̲𝙴̲̲𝚟̲̲𝚎̲̲𝚛̲ ̲𝚕̲̲𝚘̲̲𝚜̲̲𝚝̲ ̲𝚍̲̲𝚊̲̲𝚝̲̲𝚊̲ ̲𝚊̲̲𝚏̲̲𝚝̲̲𝚎̲̲𝚛̲ ̲𝚛̲̲𝚎̲̲𝚜̲̲𝚝̲̲𝚊̲̲𝚛̲̲𝚝̲̲𝚒̲̲𝚗̲̲𝚐̲ ̲𝚊̲ ̲𝙳̲̲𝚘̲̲𝚌̲̲𝚔̲̲𝚎̲̲𝚛̲ ̲𝚌̲̲𝚘̲̲𝚗̲̲𝚝̲̲𝚊̲̲𝚒̲̲𝚗̲̲𝚎̲̲𝚛̲? In this project, I tackled persistent storage challenges by integrating Docker Volumes with AWS EBS, ensuring data retention even after container restarts! 🗄️⁣
⁣
🚀 Bonus: I also automated the deployment process by integrating GitHub, AWS CodePipeline, and ECS, ensuring seamless updates with every commit!⁣
⁣
🔹 Key Achievements & Skills Learned:⁣
✅ Persistent Storage in Docker – Integrated Amazon EBS volumes with Docker containers for reliable data storage.⁣
✅ Docker Volume Management – Ensured data persistence across container restarts & terminations.⁣
✅ AWS EBS Setup & EC2 Integration – Configured block-level storage for containers running in the cloud.⁣
✅ CI/CD Automation with GitHub & AWS CodePipeline – Implemented a GitHub-triggered deployment pipeline for streamlined updates.⁣
✅ Seamless Deployment to ECS – Used Docker & AWS Elastic Container Service (ECS) for auto-deployments.⁣
✅ Advanced Troubleshooting – Resolved Docker network bridge issues by switching to host network mode for better container connectivity.⁣
⁣
⚠️ 𝐓𝐫𝐨𝐮𝐛𝐥𝐞𝐬𝐡𝐨𝐨𝐭𝐢𝐧𝐠: Docker Bridge Adapter to Host Network⁣
❌ Issue: Containers running on the default bridge network had limited connectivity, causing access issues.⁣
✔ Fix: Switched to host network mode using:⁣
⁣
𝕕𝕠𝕔𝕜𝕖𝕣 𝕣𝕦𝕟 --𝕟𝕖𝕥𝕨𝕠𝕣𝕜 𝕙𝕠𝕤𝕥 -𝕕 𝕟𝕘𝕚𝕟𝕩⁣
🔹 Why? This allows the container to use the host’s network stack, resolving communication & performance bottlenecks.⁣
