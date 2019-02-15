// เรียกกล่อง pit ทุก pit มาให้ js ใช้งาน
	pits = document.querySelectorAll('pit');

	// เวลาในการเตรียมตัว (s)
	preparing = 3;
	// ระยะเวลาที่ตุ่นจะเกิด (ms)
	birth = 1000;
	// ระยะเวลาที่ตุ่นจะอยู่รอโดนตี (ms)
	delay = 3000;

	//ฟังก์ชันหลังโหลดเว็บเสร็จ จะนับถอยหลัง 5 วินาที แล้วเริ่มเกม
	function ready(){
		// คะแนนเริ่มต้น
		score = 0;
		// เวลาในการเล่นเกม (s)
		time = 20;

		// รีเซ็ทเวลา
		updateTime();
		// รีเซ็ทคะแนนให้คนดู
		updatScore();
		// reset ทุกหลุมให้ว่าง
		for (var i = 0; i < pits.length; i++) {
			pits[i].setAttribute("status","blank");
		}

		for (let i = 0; i < preparing; i++) {
			setTimeout(
				function(){
					console.log(i);
					subTitle.innerText = "Ready! Game start in "+(preparing-i);
				},i*1000);
		}
		// หมดเวลาเตรียมตัว เรื่มเกมได้!
		setTimeout(
			function(){
				subTitle.innerText = "Play!";
				countdown();
				reloadMole();
			}
			,preparing*1000);
	}

	// สำหรับสั่งให้เวลาลด
	function countdown(){
		// ทุกๆ 1 วินาที เวลาต้องลด
		cd = setInterval(
			function(){
				// ถ้ายังไม่หมดเวลา
				if (time > 0) {
					// ลดเวลา
					time--;
					// อัพเดทเวลา
					updateTime();
				}
				// ถ้าหมดเวลา
				else{
					clearInterval(cd);
					console.log("END");
				}
			}
			,1000)
	}

	// ฟังก์ชันเกม โดยจะคอยเรียกตัวเองจนกว่าจะตาย หลักการคือ ทุกๆ เวลา birth จะมีตุ่นโผล่หน้ามา โดยสุ่มว่าจะเกิดที่ไหน จากนั้นจะรอใหโดนตีตามเวลา delay ถ้าหมดเวลา delay ยังไม่โดนตี จะหายไป
	function reloadMole(){
		// ถ้าเวลาไม่หมด ให้ทำตามนี
		if (time>0) {
			// สุ่มเลขหลุมที่จะเกิด ตั้งแต่เลข 0 ถึง 15
			var randomPit = Math.floor(Math.random() *16);

			// ตั้ง status ให้หลุมที่สุ่มได้ เป็นตุ่นโผล่มา
			pits[randomPit].setAttribute("status","mole");

			// ตั้งเวลาว่า เมื่อหมดเวลา ตุ่นจะหายไป
			setTimeout(
				function(){
					// ถ้าเวลายังไม่หมด ตุ่่นจะหาย
					if (time>0) {
						pits[randomPit].setAttribute("status","blank");
					}
				}
				,delay);
			// กำหนดหน่วงเวลาไว้ พอหมดเวลา ให้แรนดอมตุ่นออกมาต่ออีกรอบ
			setTimeout(
				function(){
				// เรียกตัวเอง
				reloadMole()
			}
			,birth);
		}
	}

    // สำหรับการตี
    function hit(pit){
    	// ตีได้ต่อเมื่อไม่หมดเวลา
    	if (time>0) {
    		// ดูว่า  status ตอนนี้คืออะไร
    		var status = pit.getAttribute("status");
    		// ถ้าตีโดนตุ่น ปรับเป็น die
    		if (status == "mole") {
    			pit.setAttribute("status","die");
    			// กดถูกได้คะแนน
    			score++;
    		}
    		// ถ้าตีโดน blank จะกลายเป็น miss
    		else if(status == "blank"){
    			pit.setAttribute("status","miss");
    			// กดิดติดลบ
    			if (time > 50){
                    score -= 5;
                }
                score--;
                time -= 2
    		}
    		// แสดงคะแนนให้คนดู
            if (score%5 == 0){
                birth -= 100;
                time += 2;
            }
            if (birth <= 100){
                birth = 1000;
            }
            if (score%7 == 0){
                delay -= 10;
            }
            if (delay < 300){
                delay = 3000;
            }
    		updatScore();
    	}
    }

    // สำรหรับโชว์คะแนน
    function updatScore(){
    	// แสดงคะแนนให้คนดู
    	theScore.innerText = score;
    }

    //สำหรับโชว์เวลา
    function updateTime(){
    	// แสดงเวลา
    	theTime.innerText = time;

    	// ถ้าหมดเวลา ให้บอก
    	if (time == 0) {
    		subTitle.innerHTML = "Time out! <a href='#!' onclick='ready()'>play again</a>";
    	}
    }



    ready();
    //comment อยากให้มีตัวตุ่นหลอกขึ้นมาครับ กดตีหักคะแนน