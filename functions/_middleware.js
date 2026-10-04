const LEGACY_MEDIA_KEYS = new Set([
  "Corresponding_angles.png",
  "aptitudeofenjoyingthingswhichyoucantunderstand.jpg",
  "askteachersgoodquestions.jpg",
  "b347244a51c40ac66479b0fa3a470b4c.png",
  "beamaverickexaminee.jpg",
  "benesse_graph_1.gif",
  "bepositivelynegative.jpg",
  "brushupyourpaststudy.jpg",
  "buildastrategyandmakeaschedule.jpg",
  "certificationtestofenglishkanjimath.jpg",
  "chantoyomu.jpg",
  "complexnumber.png",
  "dangerofhighlevelschool.jpg",
  "danglingthecarrot.jpg",
  "difficultyofobeyingmyownrules.jpg",
  "doneisbetterthanperfect.jpg",
  "dontstayseriousstayactive.jpg",
  "doyourhomeworkasap.jpg",
  "drawlinesandtranscribe.jpg",
  "everyfailureisasteppingstonetosuccess.jpg",
  "hanseisuhosei.png",
  "hardworkpaysoff.jpg",
  "heikousentohi.png",
  "howtochooseaprivateschool.jpg",
  "howtochooseastudymethod.jpg",
  "howtoconcentrateathome.jpg",
  "howtofactorizetheproblem.jpg",
  "howtogetoutofaslump.jpg",
  "howtogiveprioritytostudy.jpg",
  "howtomakeaweeklyschedule.jpg",
  "howtomakelesscarelessmistakes.jpg",
  "howtomekeawordcard.jpg",
  "howtoovercomeimpatienceandanxiety.jpg",
  "howtoovercomeweaknessesofstudy.jpg",
  "howtopullyourselftogether.jpg",
  "howtoputhomeworktogoodpracticaluse.jpg",
  "howtorealizetheentranceexam.jpg",
  "howtosetpriorities.jpg",
  "howtoshapeyourfuture.jpg",
  "howtotakeabreakfromstudy.jpg",
  "howtotakenotes.jpg",
  "howtowakeupwelltostudy.jpg",
  "improvingnaturalabilities.jpg",
  "inputandoutputofstudy.jpg",
  "instant-jhmath-provisional-10_ex1-2.png",
  "jissu.png",
  "jukeizu.png",
  "keisanmiss.jpg",
  "kouseiryokutomondaishu.jpg",
  "listentomusictostudy.jpg",
  "logo_wide.png",
  "math_classroom.jpg",
  "mathmap.pdf",
  "mathmap.png",
  "mathmap_s.png",
  "mathmapelementaryschooltohighschool.jpg",
  "numberline1.png",
  "numberline2.png",
  "pythagoras.png",
  "schedule1.png",
  "schedule2.png",
  "schedule3.png",
  "schedule4.png",
  "schedule5.png",
  "senbiki.jpg",
  "setatimenottostudy.jpg",
  "shomeinorenshu.jpg",
  "soroban.jpg",
  "strength-of-mathematics.png",
  "studyonyourown.jpg",
  "studywithfriends.jpg",
  "takeasmallstepforstudying.jpg",
  "test_j1_basic.pdf",
  "test_j2_basic.pdf",
  "test_j3_basic.pdf",
  "thedegreeofcomprehension.jpg",
  "theearlybirdcatchestheworm.jpg",
  "theprosandconsofcramschool.jpg",
  "thereforeyouarebadwhenitcounts.jpg",
  "thereisnoreasontofail.jpg",
  "thinkaboutthegoalfirst.jpg",
  "threedaysmonksyndrome.jpg",
  "triangle-circle.png",
  "understandingtosolvable.jpg",
  "whatisaptitude.jpg",
  "whattostudybeforegoingtobed.jpg",
  "yakunitatu.jpg",
]);

function objectHeaders(object) {
  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set('etag', object.httpEtag);
  headers.set('last-modified', object.uploaded.toUTCString());
  headers.set('cache-control', 'public, max-age=3600');
  return headers;
}

function decodePathname(url) {
  try {
    return decodeURIComponent(url.pathname);
  } catch {
    return null;
  }
}

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const pathname = decodePathname(url);

  if (pathname === null) return context.next();

  if (pathname.startsWith('/images/')) {
    const key = pathname.slice('/images/'.length);
    if (LEGACY_MEDIA_KEYS.has(key)) {
      return Response.redirect(new URL(`/media/${encodeURIComponent(key)}`, url.origin), 301);
    }
    return context.next();
  }

  if (!pathname.startsWith('/media/')) return context.next();

  if (request.method !== 'GET' && request.method !== 'HEAD') {
    return new Response(null, {
      status: 405,
      headers: { Allow: 'GET, HEAD' },
    });
  }

  const key = pathname.slice('/media/'.length);
  if (!key || key.includes('/')) return new Response(null, { status: 404 });

  if (request.method === 'HEAD') {
    const object = await env.MEDIA.head(key);
    if (!object) return new Response(null, { status: 404 });
    const headers = objectHeaders(object);
    headers.set('content-length', String(object.size));
    return new Response(null, { headers });
  }

  const object = await env.MEDIA.get(key);
  if (!object) return new Response(null, { status: 404 });

  const headers = objectHeaders(object);
  headers.set('content-length', String(object.size));
  return new Response(object.body, { headers });
}
